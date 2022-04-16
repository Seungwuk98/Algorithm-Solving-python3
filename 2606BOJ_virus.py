import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
graph = [[] for _ in range(a+1)]
for _ in range(b):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

result = []


def dfs(node):
    if node in result:
        return
    result.append(node)
    for i in graph[node]:
        dfs(i)


dfs(1)
print(len(result)-1)
