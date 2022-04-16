from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
mat = [[*map(int, [*input().rstrip()])]for _ in range(n)]
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
visit = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if mat[i][j] or visit[i][j]:
            continue
        visit[i][j] = True
        q = deque([(i, j)])
        r = 1
        wall = set()
        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx, ny = dx+x, dy+y
                if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                    if mat[nx][ny]:
                        wall.add((nx, ny))
                    else:
                        r += 1
                        visit[nx][ny] = True
                        q.append((nx, ny))
        for x, y in wall:
            mat[x][y] += r
for i in range(n):
    for j in range(m):
        mat[i][j] %= 10

for x in mat:
    print(''.join(map(str, x)))
