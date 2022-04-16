from heapq import *
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque([d])
    while q:
        node = q.popleft()
        if node == s:
            continue
        for prev_dist, prev_node in graph_rev[node]:
            if distance[node] == distance[prev_node] + prev_dist:
                dropped[prev_node][node] = True
                q.append(prev_node)


def dijkstra():
    heap = [(0, s)]
    distance[s] = 0
    while heap:
        dist, node = heappop(heap)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            from_start = dist+i[0]
            if distance[i[1]] > from_start and not dropped[node][i[1]]:
                distance[i[1]] = from_start
                heappush(heap, (from_start, i[1]))


while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    s, d = map(int, input().split())

    graph = [[]for _ in range(n)]
    graph_rev = [[]for _ in range(n)]

    for i in range(m):
        u, v, p = map(int, input().split())
        graph[u].append([p, v])
        graph_rev[v].append([p, u])

    dropped = [[False]*(n+1) for _ in range(n+1)]
    distance = [1e9] * (n+1)
    dijkstra()
    bfs()
    distance = [1e9] * (n+1)
    dijkstra()
    if distance[d] != 1e9:
        print(distance[d])
    else:
        print(-1)
