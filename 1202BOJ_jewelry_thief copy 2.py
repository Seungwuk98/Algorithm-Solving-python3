from heapq import *
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
gems = sorted([[*map(int, input().split())]
              for _ in range(n)])
bags = sorted([int(input())for _ in range(k)])

i = 0
heap = []
result = 0
for c in bags:
    while i < n and gems[i][0] <= c:
        heappush(heap, -gems[i][1])
        i += 1
    if heap:
        result -= heappop(heap)
print(result)
