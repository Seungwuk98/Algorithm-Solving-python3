from collections import deque
from pprint import pprint
n = int(input())
mat = [[*map(int, [*input()])]for _ in range(n)]
v = [[False]*n for _ in range(n)]
r = []
d = ((0, 1), (1, 0), (-1, 0), (0, -1))
for i in range(n):
    for j in range(n):
        if v[i][j] or not mat[i][j]:
            continue
        v[i][j] = True
        q = deque([(i, j)])
        k = 1
        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx, ny = dx+x, dy+y
                if nx < 0 or nx >= n or ny < 0 or ny >= n or v[nx][ny] or not mat[nx][ny]:
                    continue
                v[nx][ny] = True
                q.append((nx, ny))
                k += 1
        r.append(k)
r.sort()
print(len(r))
print('\n'.join(map(str, r)))
