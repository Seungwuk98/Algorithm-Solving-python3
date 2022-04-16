from heapq import *


n, m, x = map(int, input().split())
g = [[]for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    g[a].append((t, b))


def dijkstra(s):
    distance = [1e9]*(n+1)
    heap = [(0, s)]
    distance[s] = 0

    while heap:
        dist, node = heappop(heap)

        for next_dist, next_node in g[node]:
            from_start = next_dist + dist
            if from_start < distance[next_node]:
                distance[next_node] = from_start
                heappush(heap, (from_start, next_node))
    return distance


from_x = dijkstra(x)

r = 0
for i in range(1, n+1):
    dist = dijkstra(i)
    r = max(r, dist[x]+from_x[i])
print(r)
