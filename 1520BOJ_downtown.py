import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
mat = [[*map(int, input().split())]for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
d = ((1, 0), (0, 1), (-1, 0), (0, -1))


def dfs(x, y):
    if x == n-1 and y == m-1:
        dp[x][y] = 1
        return 1
    dp[x][y] = 0
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] < mat[x][y]:
            if dp[nx][ny] == -1:
                dp[x][y] += dfs(nx, ny)
                continue
            if dp[nx][ny]:
                dp[x][y] += dp[nx][ny]
    return dp[x][y]


dfs(0, 0)
print(dp[0][0])
