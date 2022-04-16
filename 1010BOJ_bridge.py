def fac(n):
    return 1 if not n else n*fac(n-1)


for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    print(fac(b)//fac(a)//fac(b-a))
