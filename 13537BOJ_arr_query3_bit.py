from bisect import bisect_right
import sys
input = sys.stdin.readline

n = int(input())
arr = [*map(int, input().split())]
bit = [[]for _ in range(n+1)]

for i in range(1, n+1):
    x = i & -i
    bit[i] = sorted(arr[i-x:i])


def query(i, j, k):
    r = 0
    while j:
        f = bisect_right(bit[j], k)
        r += len(bit[j]) - f
        j -= j & -j

    i -= 1
    while i:
        f = bisect_right(bit[i], k)
        r -= len(bit[i])-f
        i -= i & -i
    return r


for _ in range(int(input())):
    i, j, k = map(int, input().split())
    print(query(i, j, k))
