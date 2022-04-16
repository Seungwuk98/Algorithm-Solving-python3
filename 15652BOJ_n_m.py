from itertools import combinations_with_replacement
n, m = map(int, input().split())
a = combinations_with_replacement([i for i in range(1, n+1)], m)
for x in a:
    print(*x)
