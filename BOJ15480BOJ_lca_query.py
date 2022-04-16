import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n = int(input())
LOG = int(math.log2(n)) + 2

tree = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visit = [False]*(n+1)
parent = [[0]*(LOG+1)for _ in range(n+1)]
depth = [0]*(n+1)
visit[1] = True


def dfs(node, level):
    depth[node] = level

    for next in tree[node]:
        if not visit[next]:
            visit[next] = True
            parent[next][0] = node
            dfs(next, level+1)


def find_parent():
    for j in range(1, LOG+1):
        for i in range(2, n+1):
            parent[i][j] = parent[parent[i][j-1]][j-1]


def find_lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(LOG+1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a
    for i in range(LOG, -1, -1):
        if parent[a][i] != parent[b][i]:
            a, b = parent[a][i], parent[b][i]

    return parent[a][0]


dfs(1, 0)
find_parent()

for _ in range(int(input())):
    r, u, v = map(int, input().split())

    r_u = find_lca(r, u)
    u_v = find_lca(u, v)
    v_r = find_lca(v, r)
    x = r_u if depth[r_u] >= depth[u_v] else u_v
    y = v_r if depth[v_r] >= depth[x] else x
    print(y)
