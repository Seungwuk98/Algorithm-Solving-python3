import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)


def compare(p1, p2):
    x1, y1, i1 = p1
    x2, y2, i2 = p2
    c = ccw(x0, y0, x1, y1, x2, y2)
    if not c:
        if x1 == x2:
            return y1 > y2
        else:
            return x1 > x2
    return c < 0


def qsort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop(0)
    left = [x for x in arr if compare(pivot, x)]
    right = [x for x in arr if not compare(pivot, x)]
    return qsort(left) + [pivot] + qsort(right)


for _ in range(int(input())):
    q = [*map(int, input().split())]
    n = q.pop(0)
    point = []
    s = []
    i = 0
    for x in q:
        s.append(x)
        if len(s) == 2:
            s.append(i)
            point.append(s)
            s = []
            i += 1
    point.sort(reverse=True)
    x0, y0, idx = point.pop()
    point = qsort(point)
    tmp = []
    check = False
    while len(point) >= 2 and not ccw(point[-2][0], point[-2][1], point[-1][0], point[-1][1], x0, y0):
        tmp.append(point.pop())
        check = True
    if check:
        tmp.append(point.pop())
    print(idx, end=' ')
    for x, y, i in point:
        print(i, end=' ')
    for x, y, i in tmp:
        print(i, end=' ')
    print()
