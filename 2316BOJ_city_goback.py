import sys
from collections import deque
input = sys.stdin.readline

n, p = map(int, input().split())
INF = int(1e9)
cap = [[0]*(2*n+1)for _ in range(2*n+1)]  # 정점 분할, x : in, x+n : out
for i in range(1, n+1):
    cap[i][i+n] = 1
cap[2][2+n] = INF
cap[1][1+n] = INF
for _ in range(p):
    ain, bin = map(int, input().split())
    aout = ain+n
    bout = bin+n
    cap[aout][bin] = INF
    cap[bout][ain] = INF

flow = [[0]*(2*n+1)for _ in range(2*n+1)]
total = 0
sink = 2+n
while 1:
    parent = [-1]*(2*n+1)
    parent[1] = 1
    q = deque([1])
    while q and parent[sink] == -1:
        now = q.popleft()
        for next in range(1, 2*n+1):
            if cap[now][next] - flow[now][next] > 0 and parent[next] == -1:
                parent[next] = now
                q.append(next)
    if parent[sink] == -1:
        break
    now = sink
    while now != 1:
        flow[parent[now]][now] += 1
        flow[now][parent[now]] -= 1
        now = parent[now]
    total += 1
print(total)
