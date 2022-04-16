import sys
from heapq import *
input = sys.stdin.readline


def belmanford(n, edge, s):
    distance = [1e9]*(n+1)
    distance[s] = 0
    for i in range(n):
        for node, next_node, next_dist in edge:
            from_start = distance[node] + next_dist
            if distance[next_node] > from_start:
                distance[next_node] = from_start
                if i == n-1:
                    return 'YES'

    return 'NO'


for _ in range(int(input())):
    n, m, w = map(int, input().split())
    edge = []
    for __ in range(m):
        s, e, t = map(int, input().split())
        edge.append((s, e, t))
        edge.append((e, s, t))
    for __ in range(w):
        s, e, t = map(int, input().split())
        edge.append((s, e, -t))

    print(belmanford(n, edge, 1))
