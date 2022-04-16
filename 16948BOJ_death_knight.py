from collections import deque

n = int(input())
d = ((-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1))
r1, c1, r2, c2 = map(int, input().split())

q = deque([(r1, c1, 0)])
visit = [[False]*n for _ in range(n)]
visit[r1][c1] = True
while q:
    x, y, count = q.popleft()
    for dx, dy in d:
        nx, ny = dx+x, dy+y
        if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
            visit[nx][ny] = True
            if nx == r2 and ny == c2:
                print(count + 1)
                exit(0)
            q.append((nx, ny, count+1))

print(-1)
