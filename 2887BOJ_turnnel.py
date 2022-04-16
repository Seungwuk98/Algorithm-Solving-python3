import sys
from heapq import *
input = sys.stdin.readline


n = int(input())
p = []
for i in range(n):
    a, b, c = map(int, input().split())
    p.append((i, a, b, c))

g = [[]for _ in range(n)]
for j in range(1, 4):
    p.sort(key=lambda x: x[j])
    for i in range(n-1):
        p1 = p[i]
        p2 = p[i+1]
        g[p1[0]].append((abs(p1[j]-p2[j]), p2[0]))
        g[p2[0]].append((abs(p1[j]-p2[j]), p1[0]))

connected = [False]*n
edge = g[0]
heapify(edge)
result = 0
connected[0] = True
while edge:
    d, node = heappop(edge)
    if connected[node]:
        continue
    connected[node] = True
    result += d
    for next_dist, next_node in g[node]:
        if not connected[next_node]:
            heappush(edge, (next_dist, next_node))


print(result)
