import sys
import math
input = sys.stdin.readline

sys.setrecursionlimit(100000)
n = int(input())
LOG = int(math.log2(n))+2
tree = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((c, b))
    tree[b].append((c, a))

depth = [0]*(n+1)
visit = [False]*(n+1)
visit[1] = True
parent = [[0]*(LOG+1) for _ in range(n+1)]
min_road = [[1000000]*(LOG+1) for _ in range(n+1)]
max_road = [[0]*(LOG+1) for _ in range(n+1)]


def dfs(node, level):
    depth[node] = level
    for next_dist, next in tree[node]:
        if not visit[next]:
            visit[next] = True
            parent[next][0] = node
            min_road[next][0] = next_dist
            max_road[next][0] = next_dist
            dfs(next, level+1)


def find_parent():
    for j in range(1, LOG+1):
        for i in range(2, n+1):
            parent[i][j] = parent[parent[i][j-1]][j-1]
            min_road[i][j] = min(min_road[parent[i][j-1]]
                                 [j-1], min_road[i][j-1])
            max_road[i][j] = max(max_road[parent[i][j-1]]
                                 [j-1], max_road[i][j-1])


dfs(1, 0)
find_parent()
for _ in range(int(input())):
    a, b = map(int, input().split())
    if depth[a] > depth[b]:
        a, b = b, a
    x, y = a, b
    min_result = 10000000
    max_result = 0
    for i in range(LOG+1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            min_result = min(min_road[b][i], min_result)
            max_result = max(max_road[b][i], max_result)
            b = parent[b][i]

    if a == b:
        lca = a
    else:
        6
        for i in range(LOG, -1, -1):
            if parent[a][i] != parent[b][i]:
                min_result = min(min_result, min_road[a][i], min_road[b][i])
                max_result = max(max_result, max_road[a][i], max_road[b][i])
                a, b = parent[a][i], parent[b][i]
        min_result = min(min_result, min_road[a][0], min_road[b][0])
        max_result = max(max_result, max_road[a][0], max_road[b][0])
        lca = parent[a][0]

    print(min_result, max_result)
