n = int(input())
d = 1000000000


def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, (a+b) % d
    return b


if n < 0 and not n & 1:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)

print(f(abs(n)))
