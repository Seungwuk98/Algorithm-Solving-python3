def f(n):
    k = 1
    v = 2
    if n == 1:
        return k
    elif n == 2:
        return v
    x = 3
    while x <= n:
        k, v = v, (k+v) % 10007
        x += 1
    return v


print(f(int(input())))
