import sys
from bisect import bisect_right as br
input = sys.stdin.readline
n = int(input())
arr = [*map(int, input().split())]
bit = [[]for _ in range(n+1)]

for i in range(1, n+1):
    x = i & -i
    bit[i] = sorted(arr[i-x:i])

l_ans = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    a ^= l_ans
    b ^= l_ans
    c ^= l_ans
    r = 0
    while b:
        f = br(bit[b], c)
        r += len(bit[b]) - f
        b -= b & -b
    a -= 1
    while a:
        f = br(bit[a], c)
        r -= len(bit[a]) - f
        a -= a & -a
    l_ans = r
    print(r)
