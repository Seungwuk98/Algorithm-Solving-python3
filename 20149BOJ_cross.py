def check(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    c1 = ccw(x1, y1, x2, y2, x3, y3)
    c2 = ccw(x1, y1, x2, y2, x4, y4)
    c3 = ccw(x3, y3, x4, y4, x1, y1)
    c4 = ccw(x3, y3, x4, y4, x2, y2)
    x, y = solution(x1, y1, x2, y2, x3, y3, x4, y4)
    if x1 > x2:
        x1, x2 = x2, x1
    if x3 > x4:
        x3, x4 = x4, x3
    if y1 > y2:
        y1, y2 = y2, y1
    if y3 > y4:
        y3, y4 = y4, y3
    if c1 == c2 == c3 == c4 == 0:
        if x1 < x3 < x2 or x1 < x4 < x2 or x3 < x1 < x4 or x3 < x2 < x4 or y1 < y3 < y2 or y1 < y4 < y2 or y3 < y1 < y4 or y3 < y2 < y4:
            return True
        elif (x2 < x3 and (y2 < y3 or y1 > y4)) or (x1 > x4 and (y2 < y3 or y1 > y4)) or (x1 == x2 == x3 == x4 and (y2 < y3 or y1 > y4)) or (y1 == y2 == y3 == y4 and (x2 < x3 or x1 > x4)):
            return False
        elif x1 == x3 and x2 == x4 and y1 == y3 and y2 == y4:
            return True
        else:
            x1, y1, x2, y2 = line1
            x3, y3, x4, y4 = line2
            if (x1, y1) == (x3, y3) or (x1, y1) == (x4, y4):
                return x1, y1
            elif (x2, y2) == (x3, y3) or (x2, y2) == (x4, y4):
                return x2, y2
            else:
                raise
    elif (c1*c2, c3*c4) == (0, 0) and (c1 or c2 or c3 or c4):
        return x, y
    elif (c1*c2 < 0 and c3*c4 == 0) or (c1*c2 == 0 and c3*c4 < 0):
        return x, y
    elif c1*c2 < 0 and c3*c4 < 0:
        return x, y
    else:
        return False


def solution(x1, y1, x2, y2, x3, y3, x4, y4):
    mat = [[-(y2-y1), x2-x1], [-(y4-y3), x4-x3]]
    vec = [(x2-x1)*y1-(y2-y1)*x1, (x4-x3)*y3 - (y4-y3)*x3]
    x, y = mat_vector_cross(mat_rev(mat), vec)
    return x, y


def mat_rev(mat):
    det = mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
    if not det:
        return [[0, 0], [0, 0]]
    return [[mat[1][1]/det, -mat[0][1]/det], [-mat[1][0]/det, mat[0][0]/det]]


def mat_vector_cross(mat, vec):
    r = [0, 0]
    for i in range(2):
        for j in range(2):
            r[i] += mat[i][j]*vec[j]
    return r


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)


line1 = [*map(int, input().split())]
line2 = [*map(int, input().split())]

sol = check(line1, line2)
if type(sol) is tuple:
    print(1)
    print(*sol)
else:
    print(+sol)
