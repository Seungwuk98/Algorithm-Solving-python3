from itertools import permutations
from pprint import pprint
from copy import deepcopy

n, m, k = map(int, input().split())
array = [[*map(int, input().split())]for _ in range(n)]
l = []

for _ in range(k):
    r, c, s = map(int, input().split())
    l.append((r-1, c-1, s))

comb = [*permutations(l)]


def rotate(data, r, c, s):
    cop = deepcopy(data)
    d = ((0, 1), (1, 0), (0, -1), (-1, 0))
    for p in range(1, s+1):
        i, j, k = r-p, c-p, 0
        while True:
            dx, dy = d[k]
            nx, ny = i+dx, j+dy
            if nx < r-p or nx > r+p or ny < c-p or ny > c+p:
                k += 1
                continue
            cop[nx][ny] = data[i][j]
            i, j = nx, ny
            if i == r-p and j == c-p:
                break
    return cop


def value(data):
    min_value = 10000
    for x in data:
        min_value = min(min_value, sum(x))
    return min_value


min_value = 10000
for x in comb:
    data = deepcopy(array)
    for r, c, s in x:
        data = rotate(data, r, c, s)
    val = value(data)
    min_value = min(val, min_value)
if min_value == 10000:
    print(value(data))
else:
    print(min_value)
