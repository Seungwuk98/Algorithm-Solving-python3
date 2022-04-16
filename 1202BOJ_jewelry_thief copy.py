from heapq import *
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
gems = [[*map(int, input().split())]for _ in range(n)]
bags = sorted([int(input())for _ in range(k)])
heapify(gems)

heap = []
for m, v in gems:
    heappush(heap, (-v, m))
result = 0
for i in range(k):
    c = bags[i]
    while heap:
        v, m = heappop(heap)
        if m <= c:
            result -= v
            break
        else:
            heap.append((v, m))
    heapify(heap)
print(result)
