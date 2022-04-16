import math
n = int(input())
b = set([*map(int, input().split())])
n = max(b)
a = [True for i in range(n+1)]
for i in range(2, int(math.sqrt(n))+1):
    if not a[i]:
        continue
    j = 2
    while i*j <= n:
        a[i*j] = False
        j += 1
n = set([i for i in range(2, n+1) if a[i] and i > 1])

print(len(n & b))
