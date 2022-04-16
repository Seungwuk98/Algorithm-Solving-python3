import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]
for i in range(m):
    k, v = map(int, input().split())
    graph[v].append(k)
result = [0]+[1]*n

max_value = -1
for i in range(1, n+1):
    visited = [False]*(n+1)
    visited[i] = True
    q = deque([i])
    count = 1
    while q:
        node = q.popleft()
        for j in graph[node]:
            if not visited[j]:
                visited[j] = True
                q.append(j)
                count += 1
    if max_value < count:
        result = [i]
        max_value = count
    elif max_value == count:
        result.append(i)
        max_value = count


print(*result)
# max_value = max(result)
# for i in range(n+1):
#     if result[i] == max_value:
#         print(i, end=' ')
