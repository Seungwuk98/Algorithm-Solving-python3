from collections import deque
a, b = map(int, input().split())
q = deque([(a, 0)])

while q:
    x, c = q.popleft()
    for i in [x*2, x*10+1]:
        if i > b:
            continue
        if i == b:
            c += 1
            print(c+1)
            exit(0)
        q.append((i, c+1))
print(-1)
