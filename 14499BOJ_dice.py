n, m, x, y, k = map(int, input().split())

dice = [0]*6  # 0: 아래, 1: 왼, 2: 위, 3: 오, 4: 앞, 5: 뒤
d = ((), (0, 1), (0, -1), (-1, 0), (1, 0))  # 1: 동, 2: 서, 3: 북, 4: 남
mat = [[*map(int, input().split())]for _ in range(n)]


def rotate(qry):
    if qry == 1:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif qry == 2:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
    elif qry == 3:
        dice[0], dice[4], dice[2], dice[5] = dice[5], dice[0], dice[4], dice[2]
    else:
        dice[0], dice[4], dice[2], dice[5] = dice[4], dice[2], dice[5], dice[0]


def query(qry):
    global x, y
    dx, dy = d[qry]
    nx, ny = x+dx, y+dy
    if 0 <= nx < n and 0 <= ny < m:
        rotate(qry)
        x, y = nx, ny
        if not mat[nx][ny]:
            mat[nx][ny] = dice[0]
        else:
            dice[0] = mat[nx][ny]
            mat[nx][ny] = 0
        print(dice[2])


for qry in map(int, input().split()):
    query(qry)
