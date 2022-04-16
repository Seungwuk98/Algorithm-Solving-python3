a = [0, 1]
d = 10


def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    k, v = 0, 1
    for i in range(1, n):
        k, v = v, (k+v) % d
        b(v)
    return v


def b(x):
    while x:
        a.append(x % 10)
        x //= 10


f(100)
print(a)
