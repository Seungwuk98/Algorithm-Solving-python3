from heapq import *
k, n = map(int, input().split())
p = [*map(int, input().split())]
h = [i for i in p]
s = set()
count = 0
while count < n:
    node = heappop(h)
    if node in s:
        continue
    print(node, len(s))
    s.add(node)
    count += 1
    for j in p:
        now = j*node
        if now < 2**31:
            heappush(h, now)
print(node)

h = [i for i in p]
s = set([i for i in p])

for i in range(n-1):
    node = heappop(h)
    for j in p:
        now = j*node
        if now not in s and now < 2**31:
            print(node, len(s))
            s.add(now)
            heappush(h, j*node)

print(heappop(h))
