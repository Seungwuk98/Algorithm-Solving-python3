from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
mat = [[[*map(int, input().split())]for _ in range(n)]for __ in range(h)]
count = [[[0]*m for __ in range(n)] for _ in range(h)]
q = deque()
for i in range(n):
    for j in range(m):
        for k in range(h):
            if mat[k][i][j] == 1:
                q.append((k, i, j))
d = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
while q:
    z, x, y = q.popleft()
    for dx, dy, dz in d:
        nx, ny, nz = dx+x, dy+y, dz+z
        if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h or mat[nz][nx][ny]:
            continue
        count[nz][nx][ny] = count[z][x][y] + 1
        mat[nz][nx][ny] = 1
        q.append((nz, nx, ny))


def check(n, m, h, data):
    for i in range(n):
        for j in range(m):
            for k in range(h):
                if data[k][i][j] == 0:
                    return False
    return True


if check(n, m, h, mat):
    print(max([max([max(y) for y in x]) for x in count]))
else:
    print(-1)
