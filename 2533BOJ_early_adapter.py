import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
g = [[]for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

visit = [False]*(n+1)
dp = [[0]*2 for _ in range(n+1)]


def dfs(node):
    c = False
    for next in g[node]:
        if not visit[next]:
            visit[next] = True
            c = True
            dfs(next)
            dp[node][1] += min(dp[next])
            dp[node][0] += dp[next][1]
    if not c:
        dp[node][0] = 0
        dp[node][1] = 1
        return
    dp[node][1] += 1


visit[1] = True
dfs(1)
print(min(dp[1]))
