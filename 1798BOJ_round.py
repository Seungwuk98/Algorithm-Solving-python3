from heapq import *
from math import sqrt
import sys
input = sys.stdin.readline
n = int(input())
INF = int(1e9)


def angle_y(p):
    x1, y1 = p
    vec = [x1-x0, y1-y0]
    if not vec[0]:
        return (INF, x1, y1)
    else:
        return vec[1]/vec[0]


p = []
for _ in range(n):
    heappush(p, [*map(int, input().split())])
x0, y0 = heappop(p)
p.sort(key=angle_y, reverse=True)


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)


l2p = [(x0, y0), p[0]]

result = 2
for i in range(1, n-1):
    c = ccw(*l2p[0], *l2p[1], *p[i])
    if c > 0:
        l2p = [l2p[1], p[i]]
        result += 1
    else:
        l2p[1] = p[i]
if ccw(*l2p[0], *l2p[1], *[x0, y0]) == 0:
    result -= 1
print(result)
