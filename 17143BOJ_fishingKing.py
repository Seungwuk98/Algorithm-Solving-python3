import sys
from pprint import pprint
input = sys.stdin.readline


def move(i, j, v, f):
    ni, nj = i, j
    if f == 1:
        ni -= v
        if ni < 0:
            ni = abs(ni)
            f = 2
    elif f == 2:
        ni += v
    elif f == 3:
        nj += v
    else:
        nj -= v
        if nj < 0:
            nj = abs(nj)
            f = 3

    if f == 2 and ni >= r:
        x, y = divmod(ni, r-1)
        if not y:
            x -= 1
            y = r-1
        if x & 1:
            f = 1
            ni = r-y-1
        else:
            ni = y
    elif f == 3 and nj >= c:
        x, y = divmod(nj, c-1)
        if not y:
            x -= 1
            y = c-1
        if x & 1:
            f = 4
            nj = c-y-1
        else:
            nj = y
    return ni, nj, f


r, c, m = map(int, input().split())
mat = [[()for _ in range(c)]for _ in range(r)]
for _ in range(m):
    x, y, z, w, v = map(int, input().split())
    mat[x-1][y-1] = (v, z, w)
king = 0
for k in range(c):
    for i in range(r):
        if mat[i][k]:
            king += mat[i][k][0]
            mat[i][k] = ()
            break
    tmp = [[()for _ in range(c)]for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if mat[i][j]:
                s, v, f = mat[i][j]
                ni, nj, f = move(i, j, v, f)
                if tmp[ni][nj]:
                    ss, vv, ff = tmp[ni][nj]
                    tmp[ni][nj] = tmp[ni][nj] if ss > s else (s, v, f)
                else:
                    tmp[ni][nj] = (s, v, f)
    mat = tmp
print(king)
