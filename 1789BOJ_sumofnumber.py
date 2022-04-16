def f(n):
    return n*(n+1)//2


n = int(input())
s = set()
i = 1
while f(i+1) <= n:
    i += 1
print(i)
