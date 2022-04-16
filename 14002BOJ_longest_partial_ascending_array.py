import sys
from copy import deepcopy
input = sys.stdin.readline
n = int(input())
arr = [*map(int, input().split())]
rev = [0]*n
g = {}
l = 0
c = [1e9]*(n+1)
for j in range(n):
    i = arr[j]
    if l == 0:
        l += 1
        c[l] = i
        rev[j] = l
    else:
        if i > c[l]:
            c[l+1] = i
            rev[j] = l+1
            l += 1
        else:
            _min = 1
            _max = l
            while _max > _min:
                now = (_min+_max)//2

                if c[now] < i:
                    _min = now+1
                else:
                    _max = now
            if c[_min] > i:
                c[_min] = i
                rev[j] = _min
print(l)
r = []
for i in range(n-1, -1, -1):
    if rev[i] == l:
        r.append(arr[i])
        l -= 1
        if not l:
            break
r.reverse()
print(*r)
