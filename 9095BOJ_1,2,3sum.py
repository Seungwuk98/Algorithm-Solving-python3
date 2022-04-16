def f(n):
    a, b, c = 1, 2, 4
    if n == 1:
        return a
    elif n == 2:
        return b
    elif n == 3:
        return c

    for i in range(3, n):
        a, b, c = b, c, a+b+c
    return c


for _ in range(int(input())):
    n = int(input())
    print(f(n))
