import sys
input = sys.stdin.readline
n, q = map(int, input().split())
arr = [*map(int, input().split())]
bit = [0]*(n+1)
for i in range(1, n+1):
    bit[i] = sum(arr[i-(i & -i):i])


def update(i, v):
    t = arr[i-1]
    arr[i-1] = v
    add = v-t
    while i <= n:
        bit[i] += add
        i += i & -i


def interval(x, y):
    r = 0
    while y:
        r += bit[y]
        y -= y & -y
    x -= 1
    while x:
        r -= bit[x]
        x -= x & -x
    return r


for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    print(interval(x, y))
    update(a, b)
