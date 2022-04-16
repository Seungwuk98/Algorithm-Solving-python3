n, k = map(int, input().split())
D = 10007


def comb(n, k):
    if not k:
        return 1
    if not n or n < k:
        return 0
    r, s, t = 1, 1, 1
    for i in range(2, n+1):
        r = r*i % D
        if k == i:
            s = pow(r, D-2)
        if n-k == i:
            t = pow(r, D-2)
    return r*s % D*t % D


print(comb(n, k))
