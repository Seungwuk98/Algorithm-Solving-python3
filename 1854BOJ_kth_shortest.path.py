from heapq import *

n, m, k = map(int, input().split())
g = [[]for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((c, b))
distance = [[-1e9]*k for _ in range(n+1)]
distance[1][-1] = 0
max_dist = [1e9]*(n+1)


def k_dijkstra(s):
    heap = [(0, s)]
    while heap:
        dist, node = heappop(heap)

        for next_dist, next_node in g[node]:
            from_start = dist+next_dist
            if from_start <= max_dist[next_node]:
                heappushpop(distance[next_node], -from_start)
                max_dist[next_node] = -distance[next_node][0]
                heappush(heap, (from_start, next_node))


k_dijkstra(1)
for i in range(1, n+1):
    x = -distance[i][0]
    if x == 1e9:
        print(-1)
    else:
        print(x)
