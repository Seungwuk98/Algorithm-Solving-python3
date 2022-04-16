s = int(input())
c = [[*map(int, input().split())]for _ in range(s)]


def check(s, i, j):
    c0 = True
    c1 = True
    for di in range(s):
        for dj in range(s):
            nj = j+dj
            ni = i+di
            if c[ni][nj] == 1:
                c0 = False
            else:
                c1 = False
    return c0, c1


def cut(s, i, j):
    c0, c1 = check(s, i, j)
    if c0:
        return 1, 0
    elif c1:
        return 0, 1
    l0 = 0
    l1 = 0
    for di in [0, s//2]:
        for dj in [0, s//2]:
            ni = i+di
            nj = j+dj
            n0, n1 = cut(s//2, ni, nj)
            l0 += n0
            l1 += n1
    return l0, l1


l0, l1 = cut(s, 0, 0)
print(l0)
print(l1)
