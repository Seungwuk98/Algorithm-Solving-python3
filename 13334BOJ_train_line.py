import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
line = [sorted([*map(int, input().split())])for _ in range(n)]
line.sort(key=lambda x: x[1])
d = int(input())
result = 0
heap = []
for l, r in line:
    if r-l > d:
        continue
    if not heap:
        heappush(heap, (l, r))
    else:
        left = heap[0][0]
        if r <= min(left, l) + d:
            heappush(heap, (l, r))
        else:
            while heap and heap[0][0]+d < r:
                heappop(heap)
            heappush(heap, (l, r))
    result = max(result, len(heap))

print(result)
