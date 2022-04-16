from collections import deque
from heapq import *
n, m, r = map(int, input().split())
item = [0]+[*map(int, input().split())]
g = [[]for _ in range(n+1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    g[a].append((c, b))
    g[b].append((c, a))

for x in g:
    x.sort()


def bfs(start, m):
    heap = [(0, start)]
    distance = [1e9]*(n+1)
    distance[start] = 0
    while heap:
        dist, node = heappop(heap)
        for next_dist, next_node in g[node]:
            from_start = next_dist + dist
            if distance[next_node] > from_start and from_start <= m:
                distance[next_node] = from_start
                heappush(heap, (from_start, next_node))
    r = 0
    for i in range(1, n+1):
        if distance[i] != 1e9:
            r += item[i]
    return r


max_r = 0
for i in range(1, n+1):
    max_r = max(max_r, bfs(i, m))
print(max_r)
