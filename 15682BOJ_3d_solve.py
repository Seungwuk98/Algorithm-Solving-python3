from decimal import Decimal, getcontext
getcontext().prec = 60
eps = Decimal(
    '1e-50')
eps2 = Decimal('1e-30')
epsr = Decimal('0.000000001')
INF = Decimal('1000000')


def f(x):
    return a*x*x*x + b*x*x + c*x + d


def bi(bottom, up, inc):
    while (up-bottom).copy_abs() > eps:
        mid = (bottom + up) / 2
        fmid = f(mid)
        if fmid < 0:
            if inc:
                bottom = mid
            else:
                up = mid
        else:
            if inc:
                up = mid
            else:
                bottom = mid
    return up


for _ in range(int(input())):
    a, b, c, d = map(Decimal, input().split())
    if a < 0:
        a, b, c, d = -a, -b, -c, -d
    A = 3*a
    B = 2*b
    C = c
    D = B*B - 4*A*C
    if D <= 0:
        x = bi(-INF, INF, True)
        print(format(float(x), '.9f'))
        continue
    x1, x2 = (-B+D.sqrt())/(2*A), (-B-D.sqrt())/(2*A)
    if x1 > x2:
        x1, x2 = x2, x1
    r1, r2, r3 = bi(-INF, x1, True), bi(x1, x2, False), bi(x2, INF, True)
    result1 = [r1, r2, r3]
    result2 = []
    for r in result1:
        if f(r).copy_abs() <= eps2:
            check = True
            for x in result2:
                if (x-r).copy_abs() < epsr:
                    check = False
            if check:
                result2.append(r)
    for r in result2:
        print(format(float(r), '.9f'), end=' ')
    print()
