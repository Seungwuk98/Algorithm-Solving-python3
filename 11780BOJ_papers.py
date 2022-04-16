import sys
input = sys.stdin.readline
s = int(input())
paper = [[*map(int, input().split())]for _ in range(s)]


def cut(s, i, j):
    cm, cz, co = check(s, i, j)
    if cm:
        return (1, 0, 0)
    elif cz:
        return (0, 1, 0)
    elif co:
        return (0, 0, 1)
    lm, lz, lo = 0, 0, 0
    for di in (0, s//3, s//3*2):
        for dj in (0, s//3, s//3*2):
            ni, nj = di+i, dj+j
            mm, mz, mo = cut(s//3, ni, nj)
            lm += mm
            lz += mz
            lo += mo
    return lm, lz, lo


def check(s, i, j):
    cm = True
    cz = True
    co = True
    for di in range(s):
        for dj in range(s):
            ni, nj = i+di, j+dj
            if paper[ni][nj] == 1:
                cm, cz = False, False
            elif paper[ni][nj] == 0:
                cm, co = False, False
            else:
                cz, co = False, False
    return cm, cz, co


r = cut(s, 0, 0)
for _ in r:
    print(_)
