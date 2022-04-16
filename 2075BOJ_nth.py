from heapq import *

n = int(input())
heap = []
for _ in range(n):
    for x in map(int, input().split()):
        heappush(heap, x)
        if len(heap) > n:
            heappop(heap)
print(heap[0])
