import sys
from heapq import *
input = sys.stdin.readline

n, m, k = map(int, input().split())
s, d = map(int, input().split())
g = [[]for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((c, b))
    g[b].append((c, a))

for x in g:
    x.sort()


distance = [int(1e9)]*(n+1)
distance[s] = 0
heap = [(0, 0, s)]
min_road = 1000000

while heap:
    dist, road, node = heappop(heap)
    for next_dist, next in g[node]:
        from_start = next_dist+dist
        if distance[next] > from_start:
            distance[next] = from_start
            heappush(heap, (from_start, road+1, next))
            if next == d:
                min_road = road+1
print(distance[d])
distance = [[int(1e9)]*(min_road+1)for _ in range(n+1)]
distance[1][0] = 0
heap = [(0, 0, s)]
while heap:
    dist, road, node = heappop(heap)
    if road >= min_road:
        continue
    for next_dist, next in g[node]:
        from_start = next_dist+dist
        if distance[next][road+1] > from_start:
            distance[next][road+1] = from_start
            heappush(heap, (from_start, road+1, next))
tax = 0
for _ in range(k):
    tax += int(input())
    result = 100000000
    for j in range(1, min_road+1):
        result = min(result, distance[d][j] + j*tax)
    print(result)
