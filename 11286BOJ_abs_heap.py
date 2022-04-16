from heapq import *
import sys
input = sys.stdin.readline
h = []
for _ in range(int(input())):
    a = int(input())
    if a != 0:
        heappush(h, (abs(a), a))
    else:
        if not h:
            print(0)
            continue
        x, y = heappop(h)
        print(y)
