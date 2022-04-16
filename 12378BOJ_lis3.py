from bisect import bisect_left as b
n = int(input())
a = [*map(int, input().split())]
l = 0
c = [1e9]*n
for i in range(n):
    f = b(c, a[i])
    if f >= l:
        l += 1
    c[f] = min(c[f], a[i])
print(l)
