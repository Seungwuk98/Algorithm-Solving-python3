from functools import lru_cache

n = int(input())
d = 10007
dp = [[0]*(n+1) for _ in range(14)]

dp[0][1] = 52


def pow(n, c):
    r = 1
    while n:
        if n & 1:
            r = r*c % d
        c = c*c % d
        n >>= 1
    return r


@lru_cache(maxsize=None)
def comb(n, k):
    if k < 0:
        return 0
    r, s, t = 1, 1, 1
    for i in range(2, n+1):
        r = r*i % d
        if i == k:
            s = pow(d-2, r)
        if i == n-k:
            t = pow(d-2, r)
    return r*s % d*t % d


c, i, j = 52, 1, 1
result = 0
while n >= 4:
    result = (result + j*comb(13, i) % d*comb(c-4, n-4) % d) % d
    i += 1
    j *= -1
    n -= 4
    c -= 4
print(result)
