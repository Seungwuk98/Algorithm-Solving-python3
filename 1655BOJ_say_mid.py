import sys
from heapq import *
input = sys.stdin.readline
n = int(input())
mxhp = []
mnhp = []
for i in range(1, n+1):
    x = int(input())
    if not mxhp:
        heappush(mxhp, -x)
    elif -mxhp[0] > x:
        heappush(mxhp, -x)
    else:
        heappush(mnhp, x)
    if len(mnhp) > (i >> 1):
        heappush(mxhp, -heappop(mnhp))
    elif len(mxhp) > (i >> 1) + (i & 1):
        heappush(mnhp, -heappop(mxhp))
    print(-mxhp[0])
