from collections import deque
n, m = map(int, input().split())
g = [[]for _ in range(n+1)]
pointed = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    pointed[b] += 1

q = deque()

for idx, value in enumerate(pointed):
    if idx and value == 0:
        q.append(idx)

r = []
while q:
    now = q.popleft()
    r.append(now)

    for next in g[now]:
        pointed[next] -= 1
        if not pointed[next]:
            q.append(next)

print(*r)
