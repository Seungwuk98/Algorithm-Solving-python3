from collections import deque
from pprint import pprint
n = int(input())
mat = [[*map(int, input().split())]for _ in range(n)]

max_fish = 0
min_fish = 7
for i in range(n):
    for j in range(n):
        if mat[i][j] == 9:
            baby_shark = (i, j, 2, 0)
            mat[i][j] = 0
        elif mat[i][j]:
            max_fish = max(max_fish, mat[i][j])
            min_fish = min(min_fish, mat[i][j])
if max_fish == 0 or min_fish >= 2:
    print(0)
    exit(0)


def find_fish(baby_shark):
    i, j, s, b = baby_shark
    d = ((-1, 0), (0, -1), (0, 1), (1, 0))
    q = deque([(i, j, 0)])
    visit = [[False]*n for _ in range(n)]
    min_dist = 1e3
    result = []
    visit[i][j] = True
    while q:
        x, y, sec = q.popleft()

        if sec+1 > min_dist:
            result.sort()
            a, c = result[0]
            mat[c[0]][c[1]] = 0
            return a, c

        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visit[nx][ny] or mat[nx][ny] > s:
                continue
            visit[nx][ny] = True
            if mat[nx][ny] and mat[nx][ny] < s:
                min_dist = sec+1
                result.append(
                    (sec+1, (nx, ny, s+1 if (b+1)//s else s, (b+1) % s)))

            q.append((nx, ny, sec+1))
    return 0, (-1, -1, -1, -1)


count = 0
while baby_shark != (-1, -1, -1, -1):
    sec, baby_shark = find_fish(baby_shark)
    count += sec
print(count)
