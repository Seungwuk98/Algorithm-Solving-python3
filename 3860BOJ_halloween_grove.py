d = ((0, 1), (1, 0), (-1, 0), (0, -1))


def bf(w, h, grove, hole):
    distance = [[1e9]*h for _ in range(w)]
    distance[0][0] = 0
    cycle = False
    for k in range(w*h):
        for i in range(w):
            for j in range(h):
                if distance[i][j] == 1e9 or (i == w-1 and j == h-1):
                    continue
                if hole[i][j]:
                    t, x, y = hole[i][j]
                    if distance[x][y] > distance[i][j] + t:
                        distance[x][y] = distance[i][j] + t
                        if k == w*h-1:
                            cycle = True
                else:
                    for di, dj in d:
                        ni, nj = di+i, dj+j
                        if 0 <= ni < w and 0 <= nj < h and not grove[ni][nj]:
                            if distance[ni][nj] > distance[i][j] + 1:
                                distance[ni][nj] = distance[i][j] + 1
                                if k == w*h-1:
                                    cycle = True
    if cycle:
        return 'Never'
    elif distance[w-1][h-1] > 1e8:
        return 'Impossible'
    else:
        return distance[w-1][h-1]


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    g = int(input())
    grove = [[False]*h for _ in range(w)]
    for _ in range(g):
        x, y = map(int, input().split())
        grove[x][y] = True

    e = int(input())
    hole = [[()for __ in range(h)] for _ in range(w)]
    for _ in range(e):
        x1, y1, x2, y2, t = map(int, input().split())
        hole[x1][y1] = (t, x2, y2)

    print(bf(w, h, grove, hole))
