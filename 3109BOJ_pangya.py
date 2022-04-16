import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline
n, m = map(int, input().split())
mat = [[*input().strip('\n')]for _ in range(n)]
d = ((-1, 1), (0, 1), (1, 1))


def dfs(x, y, mat):
    if y == m-1:
        return True

    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == '.':
            mat[nx][ny] = '#'
            if dfs(nx, ny, mat):
                return True
            mat[nx][ny] = '.'
    return False


block = ['x']*m

cnt = 0
for i in range(n):
    cnt += +dfs(i, 0, mat)
print(cnt)
