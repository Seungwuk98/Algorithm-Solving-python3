F = [1, 1, 5] + [-1]*70


def f(n):
    if F[n] != -1:
        return F[n]
    m = n
    a = (3, 2)
    r = f(n-1) + 4*f(n-2)
    n -= 3
    k = 1
    while n > -1:
        r += a[k & 1]*f(n)
        k += 1
        n -= 1
    F[m] = r
    return r


for i in range(int(input())):
    print(f(int(input())))
