from random import randint
import sys
input = sys.stdin.readline


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
    primelist = [2, 3, 5, 7, 11]
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


n = int(input())
r = 0
for _ in range(n):
    x = 2*int(input())+1
    if miller_rabin(x):
        r += 1
print(r)
