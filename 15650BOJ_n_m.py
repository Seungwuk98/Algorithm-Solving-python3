from itertools import combinations
n, m = map(int, input().split())
a = [i for i in range(1, n+1)]
a_comb = combinations(a, m)
for x in a_comb:
    print(*x)
