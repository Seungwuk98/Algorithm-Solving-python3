import sys
from pprint import pprint
from collections import deque
def input(): return sys.stdin.readline().strip('\n')


d = ((0, 1), (1, 0), (0, -1), (-1, 0))


def key_remove(mat, keys):
    for key in keys:
        for i in range(n):
            for j in range(m):
                if mat[i][j] == key:
                    mat[i][j] = '.'
    keys.clear()


def find_door(mat, keys):
    i = j = k = 0
    door = []
    while not (i == j == 0 and k == 3):
        if mat[i][j] == '.' or 'a' <= mat[i][j] <= 'z' or mat[i][j] == '$':
            door.append((i, j))
        ni = i + d[k][0]
        nj = j + d[k][1]
        if ni < 0 or ni >= n or nj < 0 or nj >= m:
            k += 1
            continue
        i = ni
        j = nj
    return door


def bfs(start, mat, keys):
    visit = [[False]*m for _ in range(n)]
    sx, sy = start
    count = 0
    if 'a' <= mat[sx][sy] <= 'z':
        tmp = mat[sx][sy].upper()
        keys.add(tmp)
        mat[sx][sy] = '.'
    elif mat[sx][sy] == '$':
        mat[sx][sy] = '.'
        count += 1
    visit[sx][sy] = True
    q = deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visit[nx][ny] or not (mat[nx][ny] == '.' or mat[nx][ny] == '$' or 'a' <= mat[nx][ny] <= 'z'):
                continue
            visit[nx][ny] = True
            if mat[nx][ny] == '$':
                mat[nx][ny] = '.'
                count += 1
            elif 'a' <= mat[nx][ny] <= 'z':
                tmp = mat[nx][ny].upper()
                keys.add(tmp)
                mat[nx][ny] = '.'
            q.append((nx, ny))
    return count


def pprint(mat):
    for x in mat:
        print(*x)


for _ in range(int(input())):
    n, m = map(int, input().split())
    mat = [[*input()]for _ in range(n)]
    keys = {*input().upper()}
    key_remove(mat, keys)
    door = find_door(mat, keys)
    if not door:
        print(0)
        continue
    count = 0

    while True:
        for start in door:
            count += bfs(start, mat, keys)
        if not keys:
            break
        key_remove(mat, keys)
        door = find_door(mat, keys)

    print(count)
