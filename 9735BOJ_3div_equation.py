from math import *

eps = 0.00000000000001
eps2 = 0.0000001
INF = 1000001


def f(x):
    return a*x*x*x + b*x*x + c*x + d


def det(a, b, c):
    return b*b-4*a*c


for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    for i in range(-1000000, 1000001):
        if not f(i):
            break
    A = a
    B = b+A*i
    C = c+B*i
    D = det(A, B, C)
    result = [i]
    if not D:
        j = -B/(2*A)
        if abs(i-j) >= eps:
            result.append(-B/(2*A))
    elif D > 0:
        x1, x2 = (-B-sqrt(D))/(2*A), (-B+sqrt(D))/(2*A)
        if abs(x1-i) >= eps:
            result.append(x1)
        if abs(x2-i) >= eps:
            result.append(x2)
    result.sort()
    print(*result)
