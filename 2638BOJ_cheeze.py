import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline


n, m = map(int, input().split())
mat = [[*map(int, input().split())]for _ in range(n)]
cheese = 0
for i in range(n):
    for j in range(m):
        if mat[i][j]:
            cheese += 1

d = ((0, 1), (0, -1), (-1, 0), (1, 0))


def bfs(cheese, level):
    if not cheese:
        return level
    q = deque([(0, 0)])
    count = [[0]*m for _ in range(n)]
    count[0][0] = 1
    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = dx+x, dy+y
            if 0 <= nx < n and 0 <= ny < m:
                if mat[nx][ny]:
                    count[nx][ny] += 1
                    if count[nx][ny] == 2:
                        mat[nx][ny] = 0
                        cheese -= 1
                else:
                    if count[nx][ny]:
                        continue
                    else:
                        count[nx][ny] += 1
                        q.append((nx, ny))
    pprint(mat)
    return bfs(cheese, level+1)


print(bfs(cheese, 0))
