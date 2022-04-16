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
            print(2)
            from_start = next_dist + dist
            if not v_point[next_node] and not visited[node][next_node] and distance[next_node][0] > from_start:
                distance[next_node] = (from_start, node)
                heappush(heap, (from_start, next_node))

    track_now = end
    track_prev = distance[end][-1]

    print(distance)
    while track_prev != start and track_prev != -1:
        print(distance, 1)
        v_point[track_prev] = True
        visited[track_prev][track_now] = True
        track_prev = distance[track_prev][-1]
        track_now = track_prev


def bfs():
    q = deque([end])

    while q:
        node = q.popleft()
        if node == start:
            return

        for prev_dist, prev_node in graph_rev[node]:
            if distance[prev_node][0]+prev_dist == distance[node][0] and not visited[prev_node][node] and not v_point[prev_node]:
                q.append(prev_node)
                visited[prev_node][node] = True
                v_point[prev_node] = True
                break


while True:
    N, M = map(int, input().split())
    if N < 2:
        break
    start, end = map(int, input().split())
    graph = [[]for _ in range(N)]
    graph_rev = [[]for _ in range(N)]
    distance = [(1e9, -1)for _ in range(N)]
    distance[start] = (0, -1)
    visited = [[False]*N for i in range(N)]
    v_point = [False]*N

    for _ in range(M):
        u, v, p = map(int, input().split())
        graph[u].append((p, v))
        graph_rev[v].append((p, u))

    dijksra()
    min_value = distance[end][0]
    while min_value == distance[end][0]:
        print(3)
        distance = [(1e9, -1)for _ in range(N)]
        distance[start] = (0, -1)
        dijksra()
    if distance[end][0] == 1e9:
        print(-1)
    else:
        print(distance[end][0])
