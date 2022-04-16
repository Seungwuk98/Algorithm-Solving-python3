from heapq import *
import sys
a = int(input())
q = list()
for _ in range(a):
    heappush(q, int(input()))
m = 0
while len(q) > 1:
    s = heappop(q)+heappop(q)
    m += s
    heappush(q, s)
print(m)
