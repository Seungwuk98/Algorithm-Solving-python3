d = 1000000007


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def pow(n, c):
    r = 1
    while n:
        if n & 1:
            r = (r*c) % d
        c = (c*c) % d
        n >>= 1
    return r


m = int(input())
r = 0
for _ in range(m):
    a, b = map(int, input().split())
    g = gcd(a, b)
    a //= g
    b //= g
    r = (r+(b*pow(d-2, a)) % d) % d
print(r)
