import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

n = int(input())
parent = [0]*(n+1)
g = [[]for _ in range(n+1)]
visit = [False]*(n+1)
dep = [0]*(n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


def dfs(node=1):
    for next in g[node]:
        if not visit[next]:
            visit[next] = True
            dep[next] = dep[node] + 1
            parent[next] = node
            dfs(next)


dfs()
