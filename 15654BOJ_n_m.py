from itertools import permutations
n, m = map(int, input().split())
a = permutations(sorted([*map(int, input().split())]), m)
for x in a:
    print(*x)
