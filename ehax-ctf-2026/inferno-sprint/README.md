# Inferno Sprint — EHAX CTF 2026

> **Room / Challenge:** Inferno Sprint (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** EHAX CTF 2026
- **Challenge:** Inferno Sprint (miscellaneous)
- **Points:** `50`
- **Date:** `01-03-2026`

---

## My Solution

Solve script:

```python
from pwn import *
import heapq

def solve_maze(grid_hex, start_y, start_x, h, w):
    grid = [bytes.fromhex(row).decode() for row in grid_hex]

    fire_time = [[float('inf')] * w for _ in range(h)]
    pq = []
    portals = {}

    for y in range(h):
        for x in range(w):
            cell = grid[y][x]
            if cell in '123':
                speed = int(cell)
                fire_time[y][x] = 0
                heapq.heappush(pq, (0, y, x, speed))
            elif cell in 'abcde':
                if cell not in portals:
                    portals[cell] = []
                portals[cell].append((y, x))

    directions = [(-1, 0, 'W'), (1, 0, 'S'), (0, -1, 'A'), (0, 1, 'D')]


    while pq:
        time, y, x, speed = heapq.heappop(pq)
        if time > fire_time[y][x]: continue

        for dy, dx, _ in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] != '#':
                nxt_time = time + speed
                if nxt_time < fire_time[ny][nx]:
                    fire_time[ny][nx] = nxt_time
                    heapq.heappush(pq, (nxt_time, ny, nx, speed))


    queue = [(0, start_y, start_x, "")]
    visited = set([(start_y, start_x)])

    while queue:
        time, y, x, path = queue.pop(0)


        if y == 0 or y == h - 1 or x == 0 or x == w - 1:
            return path


        for dy, dx, move in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] != '#':
                if time + 1 < fire_time[ny][nx] and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    queue.append((time + 1, ny, nx, path + move))


        cell = grid[y][x]
        if cell in 'abcde':
            for py, px in portals[cell]:
                if (py, px) != (y, x):

                    if time + 1 < fire_time[py][px] and (py, px, 'portal') not in visited:
                        visited.add((py, px, 'portal'))
                        queue.append((time + 1, py, px, path + "P"))

    return ""


def main():

    r = remote('chall.ehax.in', 31337)

    for round_num in range(1, 6):

        r.recvuntil(b'SIZE ')
        w, h = map(int, r.recvline().strip().split())

        r.recvuntil(b'START ')
        start_y, start_x = map(int, r.recvline().strip().split())

        r.recvuntil(b'LIMIT ')
        limit = int(r.recvline().strip())

        grid_hex = []
        for _ in range(h):
            grid_hex.append(r.recvline().strip().decode())

        r.recvuntil(b'PATH> ')

        path = solve_maze(grid_hex, start_y, start_x, h, w)
        print(f"Round {round_num} Path: {path}")

        r.sendline(path.encode())

    r.interactive()

if __name__ == '__main__':
    main()
```
