from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[]for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
v = [False]*(n+1)
count = 0
for i in range(1, n+1):
    if v[i]:
        continue
    v[i] = True
    s = deque([i])
    while s:
        x = s.popleft()
        for y in g[x]:
            if not v[y]:
                s.append(y)
                v[y] = True
    count += 1
print(count)
