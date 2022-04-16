from bisect import bisect_left


n = int(input())
l = []
for _ in range(n):
    a, b = map(int, input().split())
    l.append((a, b))
l.sort()

c = [1e9]*n
lis = 0
idx = []
for i in range(n):
    find = bisect_left(c, l[i][1])
    idx.append(find)
    if lis <= find:
        lis += 1
    c[find] = l[i][1]
print(n-lis)
for i in range(n-1, -1, -1):
    if idx[i] == lis-1:
        lis -= 1
    else:
        print(l[i][0])
