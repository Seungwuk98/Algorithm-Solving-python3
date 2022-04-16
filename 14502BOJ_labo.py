from itertools import combinations
from collections import deque
from pprint import pprint
n, m = map(int, input().split())

mat = [[*map(int, input().split())]for _ in range(n)]
zero = []
virus = []
walls = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == 2:
            virus.append((i, j))
        elif mat[i][j] == 0:
            zero.append((i, j))
        else:
            walls += 1

d = ((1, 0), (0, 1), (-1, 0), (0, -1))

min_count = n*m


def bfs(virus, walls, max_v):
    global min_count
    q = deque(virus)
    visit = [[False]*m for _ in range(n)]
    for x, y in q:
        visit[x][y] = True
    count = len(q)
    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = dx+x, dy+y
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and not mat[nx][ny]:
                visit[nx][ny] = True
                count += 1
                q.append((nx, ny))
                if count > min_count:
                    return 0
    min_count = min(min_count, count)
    return n*m - count - walls


three_wall_comb = combinations(zero, 3)
max_v = 0
for three_wall in three_wall_comb:
    for x, y in three_wall:
        mat[x][y] = 1

    max_v = max(bfs(virus, walls+3, max_v), max_v)
    for x, y in three_wall:
        mat[x][y] = 0
print(max_v)
