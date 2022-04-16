from itertools import permutations

n, m = map(int, input().split())
c = sorted([*set(permutations(map(int, input().split()), m))])
for x in c:
    print(*x)
