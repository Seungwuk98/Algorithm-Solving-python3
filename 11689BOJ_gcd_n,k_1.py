from collections import defaultdict
n = int(input())


def pow(n, c):
    r = 1
    while n:
        if n & 1:
            r *= c
        c *= c
        n >>= 1
    return r


def phi(n, r):
    c = pow(r, n)
    return c - c//n


i = 2
d = defaultdict(int)
while i < int(n**(0.5))+1:
    if not n % i:
        d[i] += 1
        n //= i
    else:
        i += 1
if n != 1:
    d[n] += 1

r = 1
for k, v in d.items():
    r *= phi(k, v)
print(r)
