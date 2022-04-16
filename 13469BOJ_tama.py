from pprint import pprint

n, m = map(int, input().split())
mat = [[*input()]for _ in range(n)]


def dfs(idx, red, blue, level):
    global min_find
    ground = mat[idx]
    if level == 11 or level >= min_find:
        return
    c, nred, nblue = drop(ground, red, blue)
    if c == 1:
        min_find = min(min_find, level)
        return
    elif c == 0:
        return
    else:
        for _ in range(4):
            nred, nblue = rotate_point(len(mat[idx]), nred, nblue)
            idx = (idx+1) % 4
            dfs(idx, nred, nblue, level+1)


def rotate(mat, red, blue):
    x, y = len(mat), len(mat[0])
    tmp = [['']*x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            tmp[i][j] = mat[x-j-1][i]
    red = red[1], x-red[0]-1
    blue = blue[1], x-blue[0]-1
    return tmp, red, blue


def rotate_point(x, red, blue):
    return (red[1], x-red[0]-1), (blue[1], x-blue[0]-1)


def drop(mat, red, blue):
    x = len(mat)
    rx, ry = red
    bx, by = blue
    c = 2
    if ry == by:
        while bx < x:
            if mat[bx+1][by] == 'O':
                c *= 0
                bx += 1
            elif mat[bx+1][by] == '#' or bx+1 == rx:
                break
            else:
                bx += 1
    while rx < x:
        if mat[rx+1][ry] == 'O':
            c //= 2
            rx += 1
        elif mat[rx+1][ry] == '#' or (ry == by and rx+1 == bx):
            break
        else:
            rx += 1
    while bx < x:
        if mat[bx+1][by] == 'O':
            c *= 0
            bx += 1
            break
        elif mat[bx+1][by] == '#' or (ry == by and bx+1 == rx):
            break
        else:
            bx += 1
    return c, (rx, ry), (bx, by)


for i in range(n):
    for j in range(m):
        if mat[i][j] == 'R':
            red = i, j
            mat[i][j] = '.'
        elif mat[i][j] == 'B':
            blue = i, j
            mat[i][j] = '.'
mat1, red1, blue1 = mat, red, blue
mat2, red2, blue2 = rotate(mat, red, blue)
mat3, red3, blue3 = rotate(mat2, red2, blue2)
mat4, red4, blue4 = rotate(mat3, red3, blue3)
mat = [mat1, mat2, mat3, mat4]
red = [red1, red2, red3, red4]
blue = [blue1, blue2, blue3, blue4]

min_find = 11
for i in range(4):
    dfs(i, red[i], blue[i], 1)
if min_find == 11:
    print(-1)
else:
    print(min_find)
