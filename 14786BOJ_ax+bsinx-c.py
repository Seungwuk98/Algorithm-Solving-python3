import decimal
from math import *
from decimal import Decimal, getcontext

A, B, C = map(Decimal, input().split())
getcontext().prec = 120
PI = Decimal('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912')


def f(x):
    x = Decimal(x)
    return A*x + B*Decimal(dsin(x)) - C


def dsin(x):
    x = Decimal(x)
    while x > 0:
        x -= 2*PI
    while x < 0:
        x += 2*PI
    result = [x]
    x2 = x*x
    a = b = 1
    for i in range(2, 100):
        if not i & 1:
            a = i
        else:
            b = i
            result.append(-result[-1]*x2/a/b)
    return sum(result)


b = -1
u = 1
while f(b)*f(u) >= 0:
    b <<= 1
    u <<= 1

eps = 1e-100
eps = Decimal(str(eps))
b = Decimal(b)
u = Decimal(u)
while (b-u).copy_abs() > eps:
    m = (b+u)/2
    if f(m) < 0:
        b = m
    else:
        u = m

print(format((b+u)/2, '.6f'))
