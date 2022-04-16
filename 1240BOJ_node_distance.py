import os
import io
import math
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


n, m = map(int, input().split())
LOG = int(math.log2(n))+1
g = [[]for _ in range(n+1)]
for _ in range(n-1):
    u, v, d = map(int, input().split())
    g[u].append((d, v))
    g[v].append((d, u))

parent = [[0]*(LOG+1) for _ in range(n+1)]
depth = [0]*(n+1)
depth2 = [0]*(n+1)
visit = [False]*(n+1)
visit[1] = True


def dfs(node, level, level2):
    depth[node] = level
    depth2[node] = level2
    for dist, next in g[node]:
        if not visit[next]:
            visit[next] = True
            parent[next][0] = node
            dfs(next, level+dist, level2+1)


def sp():
    for i in range(1, LOG+1):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]


def lca(a, b):
    if depth2[a] > depth2[b]:
        a, b = b, a
    for i in range(LOG+1, -1, -1):
        if depth2[b]-depth2[a] >= (1 << i):
            b = parent[b][i]
    if a == b:
        return a
    for i in range(LOG, -1, -1):
        if parent[a][i] != parent[b][i]:
            a, b = parent[a][i], parent[b][i]
    return parent[a][0]


dfs(1, 0, 0)
sp()
for _ in range(m):
    u, v = map(int, input().split())
    l = lca(u, v)
    print(depth[u]+depth[v]-2*depth[l])
