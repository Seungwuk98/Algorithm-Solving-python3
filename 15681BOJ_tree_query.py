import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, r, q = map(int, input().split())
g = [[]for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

dp = [0]*(n+1)
visit = [False]*(n+1)
visit[r] = True


def dfs(node):
    for next in g[node]:
        if not visit[next]:
            visit[next] = True
            dfs(next)
            dp[node] += dp[next]
    dp[node] += 1


dfs(r)

for _ in range(q):
    u = int(input())
    print(dp[u])
