n = int(input())
MOD = 786433
a = [*map(int, input().split())]
polynomial = [[]for _ in range(1 << 19)]
polynomial[1] = a
cash = [dict() for _ in range(1 << 19)]


def poly(p):
    if len(polynomial[p]) < 2:
        return
    polynomial[p << 1] = polynomial[p][::2]
    polynomial[p << 1 | 1] = polynomial[p][1::2]
    poly(p << 1)
    poly(p << 1 | 1)


def pre(p, x):
    if len(polynomial[p]) == 1:
        return polynomial[p][0]
    if x not in cash[p]:
        cash[p][x] = (pre(p << 1, x*x % MOD) + x *
                      pre(p << 1 | 1, x*x % MOD) % MOD) % MOD
    return cash[p][x]


sz = 1
while sz <= n:
    sz <<= 1
while len(a) < sz:
    a.append(0)
poly(1)
for i in range(1, MOD):
    pre(1, i)
input()
for x in map(int, input().split()):
    if (x == 0):
        print(a[0])
    else:
        print(cash[1][x])
