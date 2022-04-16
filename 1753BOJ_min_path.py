from heapq import *
V, E = map(int, input().split())
s = int(input())
distance = [1e9]*(V+1)
distance[s] = 0
g = [[]for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    g[u].append((w, v))
heap = [(0, s)]
while heap:
    dist, node = heappop(heap)

    for next_dist, next_node in g[node]:
        from_start = next_dist + dist
        if from_start < distance[next_node]:
            distance[next_node] = from_start
            heappush(heap, (from_start, next_node))
for i in range(1, V+1):
    a = distance[i]
    if a == 1e9:
        print('INF')
    else:
        print(a)
