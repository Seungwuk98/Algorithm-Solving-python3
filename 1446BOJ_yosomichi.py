from heapq import *

n, d = map(int, input().split())
yo = [[]for _ in range(d+1)]

for _ in range(n):
    a, b, c = map(int, input().split())
    if a <= d:
        yo[a].append((c, b))

for x in yo:
    if x:
        x.sort()

distance = [1e9]*(d+1)
distance[0] = 0
heap = [(0, 0)]

while heap:
    dist, node = heappop(heap)

    next_node = node+1
    from_start = dist+1
    if next_node <= d and from_start < distance[next_node]:
        distance[next_node] = from_start
        heappush(heap, (from_start, next_node))
    if yo[node]:
        for next_dist, next_node in yo[node]:
            from_start = dist+next_dist
            if next_node <= d and from_start < distance[next_node]:
                distance[next_node] = from_start
                heappush(heap, (from_start, next_node))

print(distance[d])
