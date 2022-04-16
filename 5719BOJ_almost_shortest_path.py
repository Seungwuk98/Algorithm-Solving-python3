from heapq import *
from collections import deque
import sys
input = sys.stdin.readline


def dijksra():
    heap = [(0, start)]

    while heap:
        dist, node = heappop(heap)
        if node == end:
            continue

        for next_dist, next_node in graph[node]:
            from_start = next_dist + dist
            if not visited[node][next_node] and distance[next_node] > from_start:
                distance[next_node] = from_start
                heappush(heap, (from_start, next_node))


def bfs():
    q = deque([end])

    while q:
        node = q.popleft()
        if node == start:
            continue

        for prev_dist, prev_node in graph_rev[node]:
            if distance[prev_node]+prev_dist == distance[node] and not visited[prev_node][node]:
                q.append(prev_node)
                visited[prev_node][node] = True


while True:
    N, M = map(int, input().split())
    if N < 2:
        break
    start, end = map(int, input().split())
    graph = [[]for _ in range(N)]
    graph_rev = [[]for _ in range(N)]
    distance = [1e9]*N
    distance[start] = 0
    visited = [[False]*N for i in range(N)]

    for _ in range(M):
        u, v, p = map(int, input().split())
        graph[u].append((p, v))
        graph_rev[v].append((p, u))

    dijksra()
    bfs()
    distance = [1e9]*N
    distance[start] = 0
    dijksra()
    bfs()
    if distance[end] == 1e9:
        print(-1)
    else:
        print(distance[end])
