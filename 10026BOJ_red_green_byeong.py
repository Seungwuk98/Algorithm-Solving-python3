from collections import deque
n = int(input())
mat = [[*input()]for _ in range(n)]


d = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs():
    visit = [[False]*n for i in range(n)]
    count = 0
    for k in range(n):
        for l in range(n):
            if visit[k][l]:
                continue
            q = deque([(k, l)])
            while q:
                i, j = q.popleft()
                if visit[i][j]:
                    continue
                visit[i][j] = True
                for dx, dy in d:
                    nx = i+dx
                    ny = j+dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if mat[i][j] == mat[nx][ny] and not visit[nx][ny]:
                        q.append((nx, ny))

            count += 1
    return count


r = [bfs()]
for i in range(n):
    for j in range(n):
        if mat[i][j] == 'R':
            mat[i][j] = 'G'

r.append(bfs())
print(*r)
