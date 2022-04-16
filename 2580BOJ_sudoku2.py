mat = [[*map(int, input().split())]for _ in range(9)]
bit1 = [[False]*9 for _ in range(9)]
bit2 = [[False]*9 for _ in range(9)]
bit3 = [[False]*9 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if mat[i][j]:
            bit1[i][mat[i][j]-1] = bit2[j][mat[i][j] -
                                           1] = bit3[i//3*3+j//3][mat[i][j]-1] = True


def solve(i, j, mat, bit1, bit2, bit3):
    if i == 9:
        return True

    if mat[i][j]:
        return solve(i+(j+1)//9, (j+1) % 9, mat, bit1, bit2, bit3)

    for k in range(9):
        if bit1[i][k] or bit2[j][k] or bit3[i//3*3+j//3][k]:
            continue
        mat[i][j] = k+1
        bit1[i][k] = bit2[j][k] = bit3[i//3*3+j//3][k] = True
        if solve(i+(j+1)//9, (j+1) % 9, mat, bit1, bit2, bit3):
            return True
        bit1[i][k] = bit2[j][k] = bit3[i//3*3+j//3][k] = False
        mat[i][j] = 0
    return False


solve(0, 0, mat, bit1, bit2, bit3)
for x in mat:
    print(*x)
