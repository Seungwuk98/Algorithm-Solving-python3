from collections import deque
for _ in range(int(input())):
    n, k = map(int, input().split())
    cost = [0] + [*map(int, input().split())]
    g = [[]for _ in range(n+1)]
    pointed = [0]*(n+1)
    for __ in range(k):
        a, b = map(int, input().split())
        g[a].append(b)
        pointed[b] += 1

    w = int(input())
    q = []
    time = [0]*(n+1)
    for idx, value in enumerate(pointed):
        if value == 0 and idx:
            q.append(idx)
    if w in q:
        print(cost[w])
        continue
    q = deque(q)
    while q:
        now = q.popleft()
        for next in g[now]:
            if time[next] < time[now]+cost[now]:
                time[next] = time[now]+cost[now]
            pointed[next] -= 1
            if not pointed[next]:
                q.append(next)
                if next == w:
                    print(time[w]+cost[w])
