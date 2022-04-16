from bisect import bisect_right
import sys
import os
import io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
arr = [*map(int, input().split())]
h = {}
idx = [-1]*n
for i in range(n-1, -1, -1):
    x = arr[i]
    if x not in h:
        h[x] = i
        idx[i] = n
    else:
        idx[i] = h[x]
        h[x] = i
bit = [[]for _ in range(n+1)]

for i in range(1, n+1):
    x = i & -i
    bit[i] = sorted(idx[i-x:i])

pre = 0
for _ in range(int(input())):
    l, r = map(int, input().split())
    x, y = l-1+pre, r
    result = 0
    while y:
        f = bisect_right(bit[y], r-1)
        result += len(bit[y])-f
        y -= y & -y
    while x:
        f = bisect_right(bit[x], r-1)
        result -= len(bit[x])-f
        x -= x & -x
    sys.stdout.write(str(result)+'\n')
    pre = result
