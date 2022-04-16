from pprint import pprint

n, m, k = map(int, input().split())
mat = [[0]*m for _ in range(n)]
sticker = []


def rotate(mat):
    nn, mm = len(mat[0]), len(mat)
    ret = [[0]*mm for _ in range(nn)]
    for i in range(nn):
        for j in range(mm):
            ret[i][j] = mat[j][nn-i-1]
    return ret


def check(mat, stk, i, j):
    nnn, mmm = len(stk), len(stk[0])
    for di in range(nnn):
        for dj in range(mmm):
            if not stk[di][dj]:
                continue
            if stk[di][dj] and mat[i+di][j+dj]:
                return False
    for di in range(nnn):
        for dj in range(mmm):
            if not stk[di][dj]:
                continue
            mat[i+di][j+dj] = 1
    return True


def push(mat, stk):
    nn, mm = len(mat), len(mat[0])
    nnn, mmm = len(stk), len(stk[0])
    if nn < nnn or mm < mmm:
        return False
    c = False
    try:
        for i in range(nn-nnn):
            for j in range(mm-mmm):
                if check(mat, stk, i, j):
                    c = True
                    raise
    except:


for _ in range(k):
    x, y = map(int, input().split())
    st = [[*map(int, input().split())]for _ in range(x)]
    sticker.append(st)
