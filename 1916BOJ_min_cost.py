from heapq import *
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
g = [[]for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((c, b))

for x in g:
    x.sort()

start, end = map(int, input().split())
distance = [1e9]*(n+1)
heap = [(0, start)]

while heap:
    dist, node = heappop(heap)

    for next_dist, next_node in g[node]:
        from_start = dist+next_dist
        if from_start < distance[next_node]:
            distance[next_node] = from_start
            heappush(heap, (from_start, next_node))

print(distance[end])
