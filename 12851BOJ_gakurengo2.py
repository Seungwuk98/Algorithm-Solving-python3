from collections import deque
n, k = map(int, input().split())

q = deque([(n, 0)])
r = 0
min_count = 1e9
visit = [[0, 1e9]for _ in range(120000)]
visit[n][0] = 1
visit[n][1] = 0
min_count = 1e9
while q:
    now, count = q.popleft()
    if min_count <= count:
        break
    for i in (now-1, now+1, now*2):
        if 0 <= i < 120000:
            if visit[i][1] >= count + 1:
                visit[i][1] = count + 1
                visit[i][0] += 1
                q.append((i, count+1))
                if i == k:
                    min_count = min(min_count, count+1)

print(visit[k][1])
print(visit[k][0])
