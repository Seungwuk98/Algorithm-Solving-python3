from collections import deque

n = int(input())
cap = [[0]*52 for _ in range(52)]
flow = [[0]*52 for _ in range(52)]

for _ in range(n):
    a, b, c = input().split()
    if ord(a) < 97:
        a = ord(a)-65
    else:
        a = ord(a)-71
    if ord(b) < 97:
        b = ord(b)-65
    else:
        b = ord(b)-71
    c = int(c)
    cap[a][b] += c
    cap[b][a] += c

total = 0
while 1:
    parent = [-1]*52
    parent[0] = 0
    q = deque([0])
    while q and parent[25] == -1:
        now = q.popleft()
        for next in range(52):
            if cap[now][next] - flow[now][next] > 0 and parent[next] == -1:
                parent[next] = now
                q.append(next)
    if parent[25] == -1:
        break
    now = 25
    amount = int(1e11)
    while now:
        amount = min(amount, cap[parent[now]][now]-flow[parent[now]][now])
        now = parent[now]
    now = 25
    while now:
        flow[parent[now]][now] += amount
        flow[now][parent[now]] -= amount
        now = parent[now]
    total += amount

print(total)
