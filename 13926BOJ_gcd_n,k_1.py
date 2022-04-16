from random import randint
from collections import defaultdict


def modpow(c, n, d):
    r = 1
    while n:
        if n & 1:
            r = r*c % d
        c = c*c % d
        n >>= 1
    return r


def pow(c, n):
    r = 1
    while n:
        if n & 1:
            r *= c
        c *= c
        n >>= 1
    return r


def transform(n):
    s = 0
    d = n-1
    while not d & 1:
        d >>= 1
        s += 1
    return s, d


def gcd(a, b):
    return b if not a else gcd(b % a, a)


def miller_rabin(n):
    primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n in primelist:
        return True
    elif not n & 1:
        return False
    s, d = transform(n)
    isprime = True
    for a in primelist:
        if not primetest(n, a, s, d):
            isprime = False
            break
    return isprime


def primetest(n, a, s, d):
    if modpow(a, d, n) == 1:
        return True
    for i in range(s):
        if modpow(a, pow(2, i)*d, n) == n-1:
            return True
    return False


def g(x, c, n):
    return (x*x+c) % n


def rho(n):
    if miller_rabin(n):
        return n
    elif not n & 1:
        return 2

    x = y = randint(2, n)
    c = randint(-n, n)
    d = 1
    while d == 1:
        x = g(x, c, n)
        y = g(y, c, n)
        y = g(y, c, n)
        d = gcd(abs(x-y), n)
    return rho(d)


def factoriztion(n):
    result = defaultdict(int)
    while n > 1:
        d = rho(n)
        result[d] += 1
        n //= d
    return result


def phi(n):
    fact = factoriztion(n)
    result = 1
    for x in fact:
        k = fact[x]
        result *= pow(x, k) - pow(x, k-1)
    return result


print(phi(int(input())))
