from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write
n, k = map(int, input().rstrip().split())
board = [[*map(int, [*input().rstrip()])]for _ in range(n)]
v = [[False]*10 for _ in range(n)]
d = ((-1, 0), (1, 0), (0, 1), (0, -1))


def bfs(color, x, y):
    q = deque([(x, y)])

    v[x][y] = True
    visited = [(x, y)]

    while q:
        x1, y1 = q.popleft()

        for dx, dy in d:
            nx = x1+dx
            ny = y1+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= 10 or board[nx][ny] == 0:
                continue
            if board[nx][ny] == color and not v[nx][ny]:
                v[nx][ny] = True
                visited.append((nx, ny))
                q.append((nx, ny))
    if len(visited) >= k:
        for x2, y2 in visited:
            board[x2][y2] = 0

    return len(visited)


def remove_zero():
    for j in range(10):
        q = deque([])
        for i in range(n-1, -1, -1):
            if board[i][j] == 0:
                q.append(i)
                continue
            elif q:
                k = q.popleft()
                board[k][j] = board[i][j]
                board[i][j] = 0
                q.append(i)


while True:
    c = True
    for i in range(n):
        for j in range(10):
            if board[i][j] == 0:
                continue
            count = bfs(board[i][j], i, j)
            if k <= count:
                c = False
    if c:
        break
    remove_zero()
    v = [[False]*10 for _ in range(n)]

for i in board:
    for j in range(10):
        print(str(i[j]))
    print('\n')
