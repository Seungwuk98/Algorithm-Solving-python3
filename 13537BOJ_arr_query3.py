import sys
from bisect import bisect_right
input = sys.stdin.readline


n = int(input())
arr = [*map(int, input().split())]
bit = [[]for _ in range(n+1)]


def make_bit(n):
    size = 1
    while size < n:
        size <<= 1
    make(1, size, True)


def make(bottom, up, tail):
    if bottom == up:
        return [arr[up-1]] if up < n else []
    mid = (bottom+up)//2
    left = make(bottom, mid, True)
    right = make(mid+1, up, False)
    if not left:
        return right
    elif not right:
        return left

    i, j = 0, 0
    l1 = len(left)
    l2 = len(right)
    r = []
    while True:
        if i == l1:
            r.extend(right[j:])
            break
        elif j == l2:
            r.extend(left[i:])
            break

        if left[i] < right[j]:
            r.append(left[i])
            i += 1
        else:
            r.append(right[j])
            j += 1

    if tail and up <= n:
        bit[up] = r
    return r


make_bit(n)

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
