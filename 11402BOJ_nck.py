n, k, m = map(int, input().split())


def pow(c, n):
    r = 1
    while n:
        if n & 1:
            r = r*c % m
        c = c*c % m
        n >>= 1
    return r


def comb(n, k):
    r, s, t = 1, 1, 1
    for i in range(2, n+1):
        r = r*i % m
        if k == i:
            s = pow(r, m-2)
        if n-k == i:
            t = pow(r, m-2)
    return r*s % m*t % m


print(comb(n, k))
