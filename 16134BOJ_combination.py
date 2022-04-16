import sys
input = sys.stdin.readline
d = 1000000007
dp = [0]*4000001
dp_rev = [0]*4000001
dp[0], dp[1] = 1, 1
dp_rev[0], dp_rev[1] = 1, 1
t = 1


def pow(n, c):
    r = 1
    while n:
        if n & 1:
            r = (r*c) % d
        n >>= 1
        c = (c*c) % d
    return r


for i in range(2, 4000001):
    t = (t*i) % d
    dp[i] = t
dp_rev[4000000] = pow(d-2, dp[4000000])
for i in range(4000000, 1, -1):
    dp_rev[i-1] = dp_rev[i]*i % d


def comb(n, r):
    return (((dp[n]*dp_rev[r]) % d)*dp_rev[n-r]) % d


for _ in range(int(input())):
    n, k = map(int, input().split())
    print(comb(n, k))
