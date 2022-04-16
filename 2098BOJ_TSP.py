from collections import deque

n = int(input())
g = [[*map(int, input().split())]for _ in range(n)]
dp = [[1e9]*n for _ in range(1 << n+1)]
dp[1][0] = 0

q = deque([(0, 1)])
r = 1e9
while q:
    now, qry = q.popleft()
    if qry+1 == 1 << n and g[now][0]:
        r = min(r, dp[qry][now]+g[now][0])
    for i in range(n):
        if not (qry & (1 << i)) and g[now][i] and dp[qry | (1 << i)][i] > dp[qry][now]+g[now][i]:
            dp[qry | (1 << i)][i] = dp[qry][now] + g[now][i]
            q.append((i, qry | (1 << i)))

print(r)
