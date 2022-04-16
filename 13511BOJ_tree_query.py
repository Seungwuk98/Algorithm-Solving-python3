import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n = int(input())
LOG = int(math.log2(n))+1
tree = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((c, b))
    tree[b].append((c, a))

depth = [0]*(n+1)
depth2 = [0]*(n+1)
parent = [[0]*(LOG+1)for _ in range(n+1)]
visit = [False] * (n+1)
visit[1] = True


def dfs(node, level, level2):
    depth[node] = level
    depth2[node] = level2
    for dist, next in tree[node]:
        if not visit[next]:
            visit[next] = True
            parent[next][0] = node
            dfs(next, level+dist, level2+1)


def sps():
    for i in range(1, LOG+1):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]


def find_lca(a, b):
    if depth2[a] > depth2[b]:
        a, b = b, a
    for i in range(LOG+1, -1, -1):
        if depth2[b]-depth2[a] >= (1 << i):
            b = parent[b][i]
    if a == b:
        return a
    for i in range(LOG, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]


dfs(1, 0, 0)
sps()

for _ in range(int(input())):
    qry = [*map(int, input().split())]
    if qry[0] == 1:
        u, v = qry[1], qry[2]
        lca = find_lca(u, v)
        print(depth[u] + depth[v] - depth[lca]*2)
    else:
        u, v, k = qry[1], qry[2], qry[3]
        k -= 1
        lca = find_lca(u, v)
        if k <= depth2[u] - depth2[lca]:
            for i in range(LOG+1, -1, -1):
                if k >= (1 << i):
                    u = parent[u][i]
                    k -= (1 << i)
            print(u)
        else:
            k = depth2[u]+depth2[v] - k - 2 * depth2[lca]
            for i in range(LOG+1, -1, -1):
                if k >= (1 << i):
                    v = parent[v][i]
                    k -= (1 << i)
            print(v)
