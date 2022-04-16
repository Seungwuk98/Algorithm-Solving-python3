import sys
from bisect import *
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [*map(int, input().split())]
bit = [[]for _ in range(n+1)]
for i in range(1, n+1):
    bit[i] = sorted(arr[i-(i & -i):i])
arr.sort()


def solve(l, r, k, arr, bit):
    lo, hi = 0, n
    while lo < hi:
        mid = lo+hi >> 1
        under, below = find(l, r, arr[mid], bit)
        if below < k:
            lo = mid+1
        elif under >= k:
            hi = mid-1
        else:
            return arr[mid]
    return arr[lo]


def find(l, r, x, bit):
    under, below = 0, 0
    l -= 1
    while r:
        under += bisect_left(bit[r], x)
        below += bisect_right(bit[r], x)
        r -= r & -r
    while l:
        under -= bisect_left(bit[l], x)
        below -= bisect_right(bit[l], x)
        l -= l & -l
    return under, below


for _ in range(m):
    l, r, k = map(int, input().split())
    print(solve(l, r, k, arr, bit))
