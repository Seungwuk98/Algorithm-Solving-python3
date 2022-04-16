import sys
from heapq import *
input = sys.stdin.readline

cases = int(input())
for _ in range(cases):
    n, d, c = map(int, input().split())
    graph = [[]for _ in range(n+1)]
    distance = [1000000001]*(n+1)
    distance[c] = 0
    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([s, a])
    heap = [[0, c]]
    while heap:
        node = heappop(heap)
        if distance[node[1]] < node[0]:
            continue

        for i, j in graph[node[1]]:
            if node[0]+i < distance[j]:
                distance[j] = node[0]+i
                heappush(heap, [distance[j], j])
    count = 0
    max_value = 0
    for i in range(len(distance)):
        if distance[i] != 1000000001:
            count += 1
            if distance[i] > max_value:
                max_value = distance[i]
    print(count, max_value)
