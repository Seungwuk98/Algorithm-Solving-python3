def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)


a, b = map(int, input().split())
g = gcd(a, b)
print(g)
print(a*b//g)
