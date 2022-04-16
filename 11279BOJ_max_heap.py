from heapq import *
import sys
input = sys.stdin.readline
h = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if h:
            print(-heappop(h))
        else:
            print(0)
    else:
        heappush(h, -n)
