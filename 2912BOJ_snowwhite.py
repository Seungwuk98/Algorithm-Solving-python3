from random import randint
from bisect import bisect_left, bisect_right
import os
import io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def i(): return map(int, input().split())


n, c = i()
s = [[]for _ in range(c+1)]
arr = [*i()]
for x in range(n):
    s[arr[x]].append(x)
m = int(input())
for _ in range(m):
    a, b = i()
    half = (b-a+1) // 2
    for j in [0]*50:
        x = randint(a-1, b-1)
        y = arr[x]
        l = bisect_left(s[y], a-1)
        r = bisect_right(s[y], b-1)
        if r-l > half:
            print('yes {}'.format(y))
            break
    else:
        print('no')
