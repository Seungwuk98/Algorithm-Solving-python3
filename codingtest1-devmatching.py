def solution(r, c, con, qry):
    g = [[[False]*4 for _ in range(c+1)]for _ in range(r+1)]
    for r1, c1, r2, c2 in con:
        if r2-r1 == 1:
            g[r1][c1][3] = True
            g[r2][c2][1] = True
        elif r1-r2 == 1:
            g[r1][c1][1] = True
            g[r2][c2][3] = True
        elif c2-c1 == 1:
            g[r1][c1][2] = True
            g[r2][c2][0] = True
        else:
            g[r1][c1][0] = True
            g[r2][c2][2] = True
    result = []
    for q in qry:
        result.append(cut(g, q))
    return result


def cut(g, qry):
    r1, c1, r2, c2 = qry
    if r1 > r2:
        r1, r2 = r2, r1
    if c1 > c2:
        c1, c2 = c2, c1

    result = 0
    for i in range(c1, c2+1):
        if g[r1][i][1]:
            g[r1][i][1] = False
            g[r1-1][i][3] = False
            result += 1
        if g[r2][i][3]:
            g[r2][i][3] = False
            g[r2+1][i][1] = False
            result += 1
    for i in range(r1, r2+1):
        if g[i][c2][2]:
            g[i][c2][2] = False
            g[i][c2+1][0] = False
            result += 1
        if g[i][c1][0]:
            g[i][c1][0] = False
            g[i][c1-1][2] = False
            result += 1
    return result


r, c, con, qry = 4, 3, [[1, 1, 2, 1], [1, 2, 1, 3], [1, 3, 2, 3], [2, 2, 2, 3], [2, 2, 3, 2], [
    2, 3, 3, 3], [3, 2, 3, 3], [3, 2, 4, 2], [4, 1, 4, 2]], [[2, 2, 3, 1], [1, 2, 4, 2]]
print(solution(r, c, con, qry))


r, c, con, qry = 2, 2, [[1, 1, 1, 2], [2, 2, 1, 2], [2, 1, 1, 1], [
    2, 2, 2, 1]], [[1, 1, 2, 2], [1, 1, 2, 1], [2, 1, 2, 2]]
r, c, con, qry = 3, 3, [[1, 1, 2, 1], [2, 1, 3, 1], [1, 2, 2, 2], [2, 2, 3, 2], [
    1, 3, 2, 3], [2, 3, 3, 3]], [[1, 1, 3, 1], [1, 2, 3, 2], [1, 3, 3, 3]]
