from collections import deque
n, m, k = map(int, input().split())
t = [[int(x) for x in input()]for _ in range(n)]
v = [[0]*m for _ in range(n)]
v[0][0] = ~0
d = (1, 0), (0, 1), (-1, 0), (0, -1)
q = deque([(0, 0, 0, 1)])
while q:
    x, y, w, c = q.popleft()
    if x == n-1 and y == m-1:
        print(c)
        break
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and ~v[nx][ny] & 1 << w:
            v[nx][ny] = ~((1 << w)-1)
            if t[nx][ny]:
                if w < k:
                    q.append((nx, ny, w+1, c+1))
            else:
                q.append((nx, ny, w, c+1))
else:
    print(-1)
