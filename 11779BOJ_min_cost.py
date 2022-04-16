from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
g = [[]for _ in range(n+1)]
g_r = [[]for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((c, b))
    g_r[b].append((c, a))

for x in g:
    x.sort()
for y in g_r:
    y.sort()


start, end = map(int, input().split())
distance = [1e8+1]*(n+1)
distance[start] = 0
heap = [(0, start)]

while heap:
    dist, node = heappop(heap)

    for next_dist, next_node in g[node]:
        from_start = next_dist + dist
        if from_start < distance[next_node]:
            distance[next_node] = from_start
            heappush(heap, (from_start, next_node))
print(distance[end])
result = [end]
for node in result:
    if node == start:
        break
    for prev_dist, prev_node in g_r[node]:
        if prev_dist + distance[prev_node] == distance[node]:
            result.append(prev_node)
            break
result.reverse()
print(len(result))
print(*result)
