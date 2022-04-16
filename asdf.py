tetromino = [
    [(-12341234, 12341234)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅣ
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],  # ㄴ
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
    [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅗ
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
    [(1, 0), (0, 1), (1, 1), (2, 1)],  # ㅓ
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)]
]

n = int(input())
mat = [[*map(int, input().split())]for _ in range(4)]
vst = [[False]*n for _ in range(4)]


def use(i, j, d, c):
    for dx, dy in d:
        nx, ny = i+dx, j+dy
        vst[nx][ny] = c


def chk(i, j, d):
    for dx, dy in d:
        nx, ny = i+dx, j+dy
        if nx < 0 or nx >= 4 or ny < 0 or ny >= n or vst[nx][ny] or not mat[nx][ny]:
            return False
    return True


def value(i, j, d):
    ret = 1
    for dx, dy in d:
        nx, ny = i+dx, j+dy
        ret *= mat[nx][ny]
    return ret


mx = 0


def backtrack(i, j, val):
    global mx
    if j == n:
        mx = max(mx, val)
        return
    if vst[i][j]:
        backtrack((i+1) % 4, j+(i+1)//4, val)
        return

    for d in tetromino:
        if chk(i, j, d):
            use(i, j, d, True)
            backtrack((i+1) % 4, j+(i+1)//4, val + value(i, j, d))
            use(i, j, d, False)
    backtrack((i+1) % 4, j+(i+1)//4, val)


backtrack(0, 0, 0)
print(mx)
