import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]
for i in range(m):
    k, v = map(int, input().split())
    graph[v].append(k)
result = [0]+[1]*n
visited = []


def dfs(node):
    visited.append(node)
    if not graph[node]:
        return 1
    for i in graph[node]:
        if i in visited:
            result[node] += result[i]
        else:
            result[node] += dfs(i)
    return result[node]


visited = []
for i in range(1, n+1):
    if i in visited:
        continue
    dfs(i)
    print(result)

print(result)
max_value = max(result)
for i in range(n+1):
    if result[i] == max_value:
        print(i, end=' ')
