n = int(input())
a = [*map(int, input().split())]

m = -int(1e9)
w = 0
for i in range(n):
    if w < 0:
        w = 0
    w += a[i]
    m = max(m, w)
print(m)
