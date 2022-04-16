n = int(input())


def f(x):
    return 3*x**2 - 3*x + 1


m = 1
while f(m) < n:
    m += 1
print(m)
