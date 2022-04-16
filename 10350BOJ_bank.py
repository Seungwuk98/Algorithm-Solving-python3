n = int(input())
a = [*map(int, input().split())]
s = sum(a)
t = 0
for i in range(n):
    p = 0
    w = 0
    for j in range(i, n+i):
        w = p + a[j % n]
        if w < 0:
            q, r = -w//s, -w % s
            t += q+1 if r else q
        p = w
print(t)
