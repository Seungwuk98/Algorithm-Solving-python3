line1 = [*map(int, input().split())]
line2 = [*map(int, input().split())]


def check(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    vector1 = (x2-x1, y2-y1)
    vector2 = (x4-x1, y4-y1)
    vector3 = (x3-x1, y3-y1)
    vector4 = (x4-x3, y4-y3)
    vector5 = (x2-x3, y2-y3)
    vector6 = (x1-x3, y1-y3)
    c1 = cross(vector1, vector2) * cross(vector1, vector3)
    c2 = cross(vector4, vector5) * cross(vector4, vector6)
    if c1 > 0 or c2 > 0:
        return False
    elif (c1 == 0 and c2 < 0) or (c1 < 0 and c2 == 0):
        return True
    else:
        return True


def cross(vec1, vec2):
    return vec1[0]*vec2[1] - vec1[1]*vec2[0]


print(+check(line1, line2))
