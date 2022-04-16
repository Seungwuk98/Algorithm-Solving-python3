from itertools import combinations_with_replacement
n, m = map(int, input().split())
c = sorted(
    [*set(combinations_with_replacement(sorted([*map(int, input().split())]), m))])
for x in c:
    print(*x)
