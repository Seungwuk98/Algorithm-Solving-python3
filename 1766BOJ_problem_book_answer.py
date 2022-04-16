from heapq import *
import sys
i = sys.stdin.readline
p = sys.stdout.write

n, m = list(map(int, i().split()))
pointed = {i: 0 for i in range(1, n+1)}
pointing = {i: [] for i in range(1, n+1)}
for _ in range(m):
    k, v = map(int, i().split())
    pointed[v] += 1
    pointing[k].append(v)

result = []
q = []
for i in range(1, n+1):
    if pointed[i] == 0:
        heappush(q, i)

while q:
    node = heappop(q)
    result.append(node)
    for i in pointing[node]:
        pointed[i] -= 1
        if pointed[i] == 0:
            heappush(q, i)

for i in result:
    p(str(i) + ' ')
