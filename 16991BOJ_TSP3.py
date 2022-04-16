from collections import deque
n = int(input())


def d(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5


p = [[*map(int, input().split())]for _ in range(n)]
g = [[]for _ in range(n)]
for i in range(n-1):
    for j in range(i+1, n):
        dist = d(p[i], p[j])
        g[i].append((dist, j))
        g[j].append((dist, i))

dp = [[1e9]*n for _ in range(1 << n)]
r = 1e9
q = deque([(1, 0)])
dp[1][0] = 0
while q:
    qry, now = q.popleft()
    if qry+1 == 1 << n:
        r = min(r, dp[qry][now] + g[now][0][0])
        continue
    for next_dist, next_node in g[now]:
        if qry & ~(1 << next_node) and dp[qry | (1 << next_node)][next_node] > dp[qry][now]+next_dist:
            dp[qry | (1 << next_node)][next_node] = dp[qry][now]+next_dist
            q.append((qry | (1 << next_node), next_node))

print(r)
