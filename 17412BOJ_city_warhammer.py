import sys
from collections import deque
input = sys.stdin.readline

n, p = map(int, input().split())
cap = [[0]*n for _ in range(n)]

for _ in range(p):
    a, b = map(int, input().split())
    cap[a-1][b-1] = 1

flow = [[0]*n for _ in range(n)]
total = 0
while 1:
    parent = [-1]*n
    q = deque([0])
    while q and parent[1] == -1:
        now = q.popleft()
        for next in range(n):
            if cap[now][next]-flow[now][next] and parent[next] == -1:
                parent[next] = now
                q.append(next)
    if parent[1] == -1:
        break
    now = 1
    while now:
        flow[parent[now]][now] += 1
        flow[now][parent[now]] -= 1
        now = parent[now]
    total += 1
print(total)
