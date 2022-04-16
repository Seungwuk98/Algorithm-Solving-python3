d = 10007


def f(n):
    k, v = 1, 3
    if n == 1:
        return k
    elif n == 2:
        return v
    for i in range(2, n):
        k, v = v, (k*2+v) % d
    return v


print(f(int(input())))
