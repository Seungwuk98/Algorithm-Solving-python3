from collections import deque
n, m = map(int, input().split())
mat = [[*map(int, [*input()])]for _ in range(n)]
d = ((0, 1), (1, 0), (0, -1), (-1, 0))
visit = [[False]*m for _ in range(n)]
dist = [[0]*m for _ in range(n)]
dist[0][0] = 1
visit[0][0] = 1
q = deque([(0, 0)])
while q:
    x, y = q.popleft()
    if x == n-1 and y == m-1:
        print(dist[x][y])
        break
    for dx, dy in d:
        nx = x+dx
        ny = y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m or not mat[nx][ny] or visit[nx][ny]:
            continue
        visit[nx][ny] = True
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx, ny))
