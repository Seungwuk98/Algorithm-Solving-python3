from collections import deque
from pprint import pprint
m, n = map(int, input().split())
t = [[*map(int, input().split())]for _ in range(n)]
q = deque([])
for i in range(n):
    for j in range(m):
        if t[i][j] == 1:
            q.append((i, j))

count = [[0]*m for _ in range(n)]
d = ((0, 1), (1, 0), (0, -1), (-1, 0))
while q:
    x, y = q.popleft()

    for dx, dy in d:
        nx = x+dx
        ny = y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m or t[nx][ny]:
            continue
        t[nx][ny] = 1
        count[nx][ny] = count[x][y]+1
        q.append((nx, ny))


def check(t):
    for i in range(n):
        for j in range(m):
            if t[i][j] == 0:
                return False
    return True


if check(t):
    print(max([max(x)for x in count]))
else:
    print(-1)
