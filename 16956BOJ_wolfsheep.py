R, C = [*map(int, input().split())]
h = [input()for i in range(R)]

w = []
for i in range(R):
    for j in range(C):
        if h[i][j] == 'W':
            w.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
check = True
for x, y in w:
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if h[nx][ny] == 'S':
            check = False

if check:
    print(1)
    for i in range(R):
        print(h[i].replace('.', 'D'))
else:
    print(0)
