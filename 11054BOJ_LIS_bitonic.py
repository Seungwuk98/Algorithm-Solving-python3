from bisect import bisect_left, bisect_right
n = int(input())
ar = [*map(int, input().split())]
l = [1e9]*n
idx = [-1]*n

for i in range(n):
    j = bisect_left(l, ar[i])
    idx[i] = j
    l[j] = min(l[j], ar[i])
l = [1e9]*n
idx2 = [-1]*n
for i in range(n-1, -1, -1):
    j = bisect_left(l, ar[i])
    idx2[i] = j
    l[j] = min(l[j], ar[i])
max_v = 0
for i in range(n):
    max_v = max(max_v, idx[i]+idx2[i]+1)
print(max_v)
