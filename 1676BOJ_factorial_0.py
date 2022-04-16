x = [0, 0]


def f(n):
    for i in range(1, n+1):
        x[0] += t(i)
        x[1] += v(i)


def t(n):
    r = 0
    while not n & 1:
        n //= 2
        r += 1
    return r


def v(n):
    r = 0
    while not n % 5:
        n //= 5
        r += 1
    return r


f(int(input()))
print(min(x))
