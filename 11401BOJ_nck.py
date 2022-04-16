d = 1000000007


def pow(c, n):
    r = 1
    while n:
        if n & 1:
            r = r*c % d
        c = c*c % d
        n >>= 1
    return r


def comb(n, k):
    r, s, t = 1, 1, 1
    for i in range(2, n+1):
        r = r*i % d
        if i == k:
            s = pow(r, d-2)
        if i == n-k:
            t = pow(r, d-2)
    return r*s % d*t % d


n, k = map(int, input().split())
print(comb(n, k))
