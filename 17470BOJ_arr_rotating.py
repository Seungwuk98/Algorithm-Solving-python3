from pprint import pprint

n, m, r = map(int, input().split())
mat = [[*map(int, input().split())]for _ in range(n)]

t = [[(0, 0), (0, m//2)], [(n//2, 0), (n//2, m//2)]]


def x(t):
    t[0], t[1] = t[1], t[0]


def y(t):
    t[0][0], t[0][1] = t[0][1], t[0][0]
    t[1][0], t[1][1] = t[1][1], t[1][0]


def cw(t):
    t[0][0], t[0][1], t[1][1], t[1][0] = t[1][0], t[0][0], t[0][1], t[1][1]


def ccw(t):
    t[0][0], t[0][1], t[1][1], t[1][0] = t[0][1], t[1][1], t[1][0], t[0][0]


f = [0, x, y, cw, ccw]
for _ in range(r):
    a = int(input())
    f[a](t)

result = [[0]*m for _ in range(n)]
for i in range(2):
    for j in range(2):
        a, b = t[i][j]
        for di in range(n//2):
            for dj in range(m//2):
                result[i*(n//2)+di][j*(m//2)+dj] = mat[a+di][b+dj]
for u in result:
    print(*u)
