from heapq import *
from collections import deque

# 플루이드 와샬 -> 유용
# 모든 거임
# 다익스트라
# mst
# 벨만 포드 -> 음의 간선 무한순환
# 강한 결합 요소 -> 순환이 있는지
# 네트워크 플로우 -> 해당 간선을 통과한 최대의 유량


v, e = map(int, input().split())
k = int(input())
g = [[]for _ in range(v+1)]
g_r = [[]for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append((c, b))
    g_r[b].append((c, a))

for x in g:
    x.sort()


heap = [(0, k)]
distance = [1e9]*(v+1)
distance[k] = 0
while heap:
    dist, node = heappop(heap)

    for next_dist, next_node in g[node]:
        from_start = next_dist+dist
        if distance[next_node] > from_start:
            distance[next_node] = from_start
            heappush(heap, (from_start, next_node))

for i in distance[1:]:
    if i == 1e9:
        print('INF')
    else:
        print(i)


def bfs(node):
    q = deque([node])
    print(node)
    while q:
        node = q.popleft()

        for prev_dist, prev_node in g_r[node]:
            if prev_dist + distance[prev_node] == distance[node]:
                print(prev_node)
                q.append(prev_node)
                break


bfs(4)
