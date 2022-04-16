import sys
from collections import deque
input = sys.stdin.readline
n, k, d = map(int, input().split())

cap = [[0]*(n+d+2)for _ in range(n+d+2)]
for i in range(1, n+1):
    cap[0][i] = k

limit = [*map(int, input().split())]
for i in range(d):
    cap[i+n+1][n+d+1] = limit[i]

for i in range(1, n+1):
    food = [*map(int, input().split())]
    for j in range(1, food[0]+1):
        cap[i][food[j]+n] = 1

flow = [[0]*(n+d+2)for _ in range(n+d+2)]

total = 0
while 1:
    q = deque([0])
    parent = [-1]*(n+d+2)
    parent[0] = 0
    while q and parent[n+d+1] == -1:
        now = q.popleft()
        for next in range(n+d+2):
            if cap[now][next]-flow[now][next] > 0 and parent[next] == -1:
                parent[next] = now
                q.append(next)
    if parent[n+d+1] == -1:
        break
    now = n+d+1
    amount = int(1e9)
    while now:
        amount = min(amount, cap[parent[now]][now]-flow[parent[now]][now])
        now = parent[now]
    now = n+d+1
    while now:
        flow[parent[now]][now] += amount
        flow[now][parent[now]] -= amount
        now = parent[now]
    total += amount
print(total)
