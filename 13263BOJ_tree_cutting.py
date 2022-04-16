from decimal import Decimal
from bisect import bisect_left
n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
dp = [0]*n


def solve(a1, b1, a2, b2):
    return Decimal(b1-b2)/Decimal(a2-a1)


def fx(a, b, x):
    return a*x + b


f = [(b[0], 0)]
x = [int(-1e15)]

for i in range(1, n):
    m = bisect_left(x, a[i]) - 1
    dp[i] = fx(*f[m], a[i])
    while f and solve(*f[-1], b[i], dp[i]) < x[-1]:
        f.pop()
        x.pop()
    t = solve(*f[-1], b[i], dp[i])
    f.append((b[i], dp[i]))
    x.append(t)

print(dp[-1])
