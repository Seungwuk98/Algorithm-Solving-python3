def f(n):
    if n <= 1:
        return 1
    r = 1
    for i in range(1, n+1):
        r *= i
    return r


def c(n, m):
    return f(n)//f(m)//f(n-m)


n, m = map(int, input().split())
print(c(n, m))
