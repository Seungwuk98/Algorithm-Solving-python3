from itertools import *
n, k = map(int, input().split())
print(len([*combinations(range(n), k)]))
