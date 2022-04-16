from heapq import *

n, e = map(int, input().split())
g = [[]for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append((c, b))
    g[b].append((c, a))

v1, v2 = map(int, input().split())


def dijkstra(start, end):
    distance = [1e9]*(n+1)
    distance[start] = 0

    heap = [(0, start)]
    while heap:
        dist, node = heappop(heap)

        for next_dist, next_node in g[node]:
            from_start = next_dist+dist
            if from_start < distance[next_node]:
                distance[next_node] = from_start
                heappush(heap, (from_start, next_node))
    return distance[end]


v1_v2 = dijkstra(v1, v2)
d1 = dijkstra(1, v1) + v1_v2 + dijkstra(v2, n)
d2 = dijkstra(1, v2) + v1_v2 + dijkstra(v1, n)
if d1 >= 1e9:
    print(-1)
else:
    print(min(d1, d2))
