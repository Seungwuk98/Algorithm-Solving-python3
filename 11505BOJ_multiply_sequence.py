import sys
input = sys.stdin.readline
d = 1000000007
n, m, k = map(int, input().split())
zero = [False] * (n+1)
arr = [0]*n
for i in range(n):
    arr[i] = int(input())
    if not arr[i]:
        zero[i+1] = True
bit = [1]*(n+1)
zero_bit = [0]*(n+1)
for i in range(1, n+1):
    for j in range(i-(i & -i), i):
        bit[i] = (bit[i]*arr[j]) % d
        if not arr[j]:
            zero_bit[i] += 1


def update(b, c):
    t = b
    if zero[b] and not c:
        return
    elif zero[b]:
        zero[b] = False
        tmp = arr[b-1]
        arr[b-1] = c
        rev = pow(tmp, d-2)
        while t <= n:
            bit[t] = (((bit[t]*rev) % d)*c) % d
            zero_bit[t] -= 1
            t += (t & -t)
    elif not c:
        zero[b] = True
        while t <= n:
            zero_bit[t] += 1
            t += (t & -t)
    else:
        tmp = arr[b-1]
        arr[b-1] = c
        rev = pow(tmp, d-2)
        while t <= n:
            bit[t] = (((bit[t]*rev) % d)*c) % d
            t += (t & -t)


def pow(c, n):
    r = 1
    while n:
        if n & 1:
            r = (r*c) % d
        c = (c*c) % d
        n >>= 1
    return r


def mult(u):
    r = 1
    t = u
    zeros = 0
    while t > 0:
        r = (r*bit[t]) % d
        zeros += zero_bit[t]
        t -= (t & -t)
    return r, zeros


for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    else:
        r_b, zeros_b = mult(b-1)
        r_c, zeros_c = mult(c)
        if zeros_b != zeros_c:
            print(0)
        else:
            if b > c:
                b, c = c, b
            rev = pow(r_b, d-2)
            print((r_c*rev) % d)
