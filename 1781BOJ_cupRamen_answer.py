from collections import deque
from heapq import *
import sys
input = sys.stdin.readline
a = int(input())
b = deque(sorted([[*map(int, input().split())]
                  for _ in range(a)]))

i = 0
heap = []
for node in b:
    heappush(heap, node[1])
    if node[0] <= i:
        heappop(heap)
        continue
    i += 1


print(sum(heap))
