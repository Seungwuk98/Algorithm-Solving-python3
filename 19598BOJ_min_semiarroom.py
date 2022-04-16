from heapq import *

n = int(input())
seminar = sorted([[*map(int, input().split())]
                 for _ in range(n)])
max_v = n
min_v = 1

while max_v > min_v:
    now = (max_v+min_v)//2
    heap = [(0, i)for i in range(now)]
    c = True
    for s, e in seminar:
        last, idx = heappop(heap)
        if last > s:
            c = False
            break
        heappush(heap, (e, idx))

    if c:
        max_v = now
    else:
        min_v = now+1

print(max_v)
