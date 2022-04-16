n = int(input())
m = [[*input()]for _ in range(n)]


def quadtree(s, i, j):
    x = []
    c = check(s, i, j)
    if c:
        return c

    for di in (0, s//2):
        for dj in (0, s//2):
            ni, nj = i+di, j+dj
            x.append(quadtree(s//2, ni, nj))
    return '({})'.format(''.join(x))


def check(s, i, j):
    c0, c1 = True, True
    for di in range(s):
        for dj in range(s):
            ni, nj = i+di, j+dj
            if m[ni][nj] == '1':
                c0 = False
            else:
                c1 = False
    return '0' if c0 else '1' if c1 else ''


print(quadtree(n, 0, 0))
