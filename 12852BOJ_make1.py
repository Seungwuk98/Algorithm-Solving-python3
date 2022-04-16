from collections import deque
n = int(input())
if n == 1:
    print(0)
    print(1)
    exit(0)

visit = [0]*(n+1)
q = deque([n])

while q:
    now = q.popleft()
    x = []
    if not now % 3:
        x.append(now//3)
    if not now % 2:
        x.append(now//2)
    x.append(now-1)
    c = False
    for i in x:
        if not visit[i]:
            visit[i] = now
            q.append(i)
            if i == 1:
                c = True
                break
    if c:
        break

y = 1
r = [1]
while y != n:
    y = visit[y]
    r.append(y)
r.reverse()
print(len(r)-1)
print(*r)
