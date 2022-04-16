from itertools import combinations_with_replacement
n, m = map(int, input().split())
a = combinations_with_replacement(sorted([*map(int, input().split())]), m)
for x in a:
    print(*x)
