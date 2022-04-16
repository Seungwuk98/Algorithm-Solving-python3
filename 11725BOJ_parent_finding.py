from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = [[]for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])

while q:
    node = q.popleft()

    for next_node in graph[node]:
        if not parent[next_node]:
            parent[next_node] = node
            q.append(next_node)

print('\n'.join(map(str, parent[2:])))
