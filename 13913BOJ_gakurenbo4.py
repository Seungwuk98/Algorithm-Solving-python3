from collections import deque

n, k = map(int, input().split())

visit = [-1]*(1000001)
visit[n] = 0

q = deque([(n, 0)])

try:
    while q:
        now, count = q.popleft()
        for next in (now-1, now+1, 2*now):
            if 0 <= next <= 1000000 and visit[next] == -1:
                visit[next] = count + 1
                q.append((next, count + 1))
                if next == k:
                    raise
except:
    pass
print(visit[k])
q = deque([k])
result = [k]
try:
    while q:
        now = q.popleft()
        plist = (now-1, now+1) if now & 1 else (now-1, now+1, now//2)
        for prev in plist:
            if 0 <= prev <= 1000000 and visit[prev] == visit[now] - 1:
                q.appendleft(prev)
                result.append(prev)
                if prev == n:
                    raise
                break

except:
    pass
result.reverse()
print(*result)
