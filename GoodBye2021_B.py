from random import randrange
from math import gcd
import sys
import random
input = sys.stdin.readline
def print(x): return sys.stdout.write('{}\n'.format(x))


def witness(a, n, s):
    if a >= n:
        a %= n
    if a <= 1:
        return True
    d = n >> s
    x = pow(a, d, n)
    if x == 1 or x == n-1:
        return True
    for ITER in range(s):
        x = x*x % n
        if x == 1:
            return False
        if x == n-1:
            return True
    return False


def millerrabin(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    d = n >> 1
    s = 1
    while (d & 1) == 0:
        d >>= 1
        s += 1
    candidate = [2, 7, 61] if n < 4759123141 else\
        [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    return all(witness(x, n, s) for x in candidate)


def rho(n):
    x = randrange(1, n)
    c = randrange(1, n)
    g, y = 1, x
    while g == 1:
        x = (x*x+c) % n
        y = (y*y+c) % n
        y = (y*y+c) % n
        g = gcd(abs(x-y), n)
    if g == n:
        return rho(n)
    return g


def factorize(n):
    ret = dict()
    if n == 1:
        return ret
    if n % 2 == 0:
        ret[2] = 1
        n >>= 1
    if millerrabin(n):
        ret[n] = 1
        return ret
    f = rho(n)
    return factorize(f) + factorize(n//f)


def divisions(n):
    result = factorize(n)
    sn = int(n**0.5)
    a = [1]
    ret = [1]
    for x in result:
        n = result[x]
        while n:
            a.append(a[-1]*x)
            n -= 1
        tmp = []
        for i in a:
            for j in ret:
                k = i*j
                if k <= sn:
                    tmp.append(k)
        ret = tmp
        a = [1]
    return ret


for _ in range(int(input())):
    n = int(input())
    if not (1+n) % 3 or (not n & 1 and not (2 + n//2) % 3) or (not n % 9):
        print('TAK')
        continue
    sn = int(n**0.5)
    c = False
    for x in divisions(n):
        y = n//x
        if not (x+y) % 3:
            c = True
            break
    if c:
        print('TAK')
    else:
        print('NIE')
