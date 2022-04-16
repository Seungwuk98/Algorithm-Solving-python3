from heapq import *
import sys as s
i = s.stdin.readline
p = s.stdout.write
a = int(i())
b = list()
for _ in range(a):
    value = int(i())
    if value == 0 and len(b) == 0:
        p(str(0)+'\n')
    elif value == 0:
        p(str(heappop(b))+'\n')
    else:
        heappush(b, value)
