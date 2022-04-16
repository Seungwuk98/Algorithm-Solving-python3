import sys
p, q = lambda: map(int, q().split()), sys.stdin.readline
n, m = p()
a = [0]*n
b = [0]*(n+1)


def u(i, v):
    t = a[i-1]
    a[i-1] = v
    while i <= n:
        b[i] += v-t
        i += i & -i


def v(x, y, r):
    while y:
        r += b[y]
        y -= y & -y
    while x:
        r -= b[x]
        x -= x & -x
    print(r)


for _ in [0]*m:
    x, y, z = p()
    if x > y:
        x, y = y, x
    if not x:
        v(y-1, z, 0)
    else:
        u(y, z)
