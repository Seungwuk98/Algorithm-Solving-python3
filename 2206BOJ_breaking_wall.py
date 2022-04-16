from collections import deque
from pprint import pprint

n, m = map(int, input().split())
if n == 1 and m == 1:
    print(1)
    exit(0)
mat = [[*map(int, [*input()])]for _ in range(n)]
visit1 = [[False]*m for _ in range(n)]
visit2 = [[False]*m for _ in range(n)]
visit2[0][0] = True
count = [[1]*m for _ in range(n)]
q = deque([(0, 0, False)])
d = ((0, 1), (1, 0), (0, -1), (-1, 0))
while q:
    x, y, br = q.popleft()

    for dx, dy in d:
        nx, ny = dx+x, dy+y
        if 0 <= nx < n and 0 <= ny < m and not visit2[nx][ny]:
            if mat[nx][ny] and not br and not visit1[nx][ny]:
                visit1[nx][ny] = True
                count[nx][ny] = count[x][y] + 1
                q.append((nx, ny, True))
            elif not mat[nx][ny]:
                if br and not visit1[nx][ny]:
                    visit1[nx][ny] = True
                    q.append((nx, ny, br))
                elif not br:
                    visit1[nx][ny] = True
                    visit2[nx][ny] = True
                    q.append((nx, ny, br))
                count[nx][ny] = count[x][y] + 1
            if nx == n-1 and ny == m-1:
                print(count[nx][ny])
                exit(0)
print(-1)
