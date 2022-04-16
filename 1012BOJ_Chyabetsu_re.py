from collections import deque

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    r = [[False]*n for i in range(m)]
    b = []
    for __ in range(k):
        x, y = map(int, input().split())
        r[x][y] = True
        b.append((x, y))

    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    result = 0
    v = [[False]*n for i in range(m)]
    for i in b:
        if v[i[0]][i[1]]:
            continue
        q = deque([(i[0], i[1])])
        while q:
            x, y = q.popleft()

            for dx, dy in d:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if not v[nx][ny] and r[nx][ny]:
                    v[nx][ny] = True
                    q.append((nx, ny))
        result += 1
    print(result)
