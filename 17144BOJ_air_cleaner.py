from pprint import pprint
from copy import deepcopy
r, c, t = map(int, input().split())
d = ((0, 1), (1, 0), (0, -1), (-1, 0))
mat = [[*map(int, input().split())]for _ in range(r)]
clean = [-1, -1]

p = False
for i in range(r):
    for j in range(c):
        if mat[i][j] == -1:
            clean[0] = i
            clean[1] = i+1
            p = True
            break
    if p:
        break


def diffusion(mat):
    tmp = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if mat[i][j] == -1:
                continue
            tmp[i][j] = mat[i][j]//5
    for i in range(r):
        for j in range(c):
            for di, dj in d:
                ni, nj = i+di, j+dj
                if 0 <= ni < r and 0 <= nj < c and tmp[ni][nj] and mat[i][j] != -1:
                    mat[i][j] += tmp[ni][nj]
                    mat[ni][nj] -= tmp[ni][nj]


def cleaner(mat):
    tmp = deepcopy(mat)
    direction = 0
    i, j = 0, 0
    while not (i == 0 and j == 0 and direction == 3):
        di, dj = d[direction]
        ni, nj = i+di, j+dj
        if ni < 0 or ni > clean[0] or nj < 0 or nj >= c:
            direction += 1
            continue
        if mat[ni][nj] == -1 and mat[i][j] != -1:
            tmp[i][j] = 0
        elif mat[i][j] != -1 and mat[ni][nj] != -1:
            tmp[i][j] = mat[ni][nj]
        i, j = ni, nj
    direction = 0
    i, j = clean[1], 0
    while not (i == clean[1] and j == 0 and direction == 3):
        di, dj = d[direction]
        ni, nj = i+di, j+dj
        if ni < clean[1] or ni >= r or nj < 0 or nj >= c:
            direction += 1
            continue
        if mat[ni][nj] != -1 and mat[i][j] == -1:
            tmp[ni][nj] = 0
        elif mat[i][j] != -1 and mat[ni][nj] != -1:
            tmp[ni][nj] = mat[i][j]
        i, j = ni, nj
    return tmp


for _ in range(t):
    diffusion(mat)
    mat = cleaner(mat)
print(2 + sum([sum(x) for x in mat]))
