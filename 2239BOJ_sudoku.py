mat = [[*map(int, [*input()])]for _ in range(9)]
qry1 = [0]*9
qry2 = [0]*9
qry3 = [[0]*3 for _ in range(3)]

for i in range(9):
    for j in range(9):
        if mat[i][j]:
            qry1[i] |= 1 << mat[i][j]
            qry2[j] |= 1 << mat[i][j]
            qry3[i//3][j//3] |= 1 << mat[i][j]


def dfs(i, j, mat, qry1, qry2, qry3):
    if i == 9:
        for x in mat:
            print(''.join(map(str, x)))
        exit(0)

    if mat[i][j]:
        dfs(i+(j+1)//9, (j+1) % 9, mat,  qry1, qry2, qry3)
        return

    for k in range(1, 10):
        if (qry1[i] & (1 << k)) or (qry2[j] & (1 << k)) or (qry3[i//3][j//3] & (1 << k)):
            continue
        mat[i][j] = k
        qry1[i] |= 1 << k
        qry2[j] |= 1 << k
        qry3[i//3][j//3] |= 1 << k
        dfs(i+(j+1)//9, (j+1) % 9, mat, qry1, qry2, qry3)
        mat[i][j] = 0
        qry1[i] &= ~(1 << k)
        qry2[j] &= ~(1 << k)
        qry3[i//3][j//3] &= ~(1 << k)


dfs(0, 0, mat, qry1, qry2, qry3)
