from itertools import combinations
t = int(input())
n = int(input())
a = [*map(int, input().split())]
m = int(input())
b = [*map(int, input().split())]

pre_a = [0]*(n+1)
pre_b = [0]*(m+1)

for i in range(1, n+1):
    pre_a[i] = pre_a[i-1] + a[i-1]
for j in range(1, m+1):
    pre_b[j] = pre_b[j-1] + b[j-1]

i1, j1 = 0, 1
i2, j2 = 0, 1

b_comb = combinations(pre_b, 2)
a_comb = combinations(pre_a, 2)
a_subsum = {}
b_subsum = {}

for x, y in a_comb:
    if y-x not in a_subsum:
        a_subsum[y-x] = 0
    a_subsum[y-x] += 1

r = 0
for x, y in b_comb:
    if t - (y-x) in a_subsum:
        r += a_subsum[t-(y-x)]
print(r)
