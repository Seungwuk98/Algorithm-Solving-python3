import sys
import math
input = sys.stdin.readline

sys.setrecursionlimit(100000)
LOG = 18


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


def lca(a, b):
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


def dist(a, b):
    return depth[a] + depth[b] - depth[lca(a, b)]


for _ in range(int(input())):
    n, q, r = map(int, input().split())
    tree = [[]for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    depth = [0]*(n+1)
    visit = [False]*(n+1)
    visit[1] = True
    parent = [[0]*(LOG+1) for _ in range(n+1)]

    dfs(1, 0)
    find_parent()
    for _ in range(q):
        s, u = map(int, input().split())
        if s:
