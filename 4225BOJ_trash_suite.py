import sys
import math
input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)


def compare(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    c = ccw(x0, y0, x1, y1, x2, y2)
    if c != 0:
        return c < 0
    else:
        if x1 == x2:
            return y1 > y2
        else:
            return x1 > x2


def asort(p):
    if len(p) <= 1:
        return p

    pivot = p[0]
    left = [x for x in p[1:] if compare(pivot, x)]
    right = [x for x in p[1:] if not compare(pivot, x)]
    return asort(left) + [pivot] + asort(right)


def convex(p):
    s = [(x0, y0)]
    i = 0
    for i in range(n-1):
        while len(s) >= 2 and ccw(*s[-2], *s[-1], *p[i]) <= 0:
            s.pop()
        s.append(p[i])
    if not ccw(*s[-2], *s[-1], x0, y0):
        s.pop()
    return s


def width(s):
    m = len(s)
    minw = int(1e9)
    for i in range(m):
        p1, p2 = s[i-1], s[i]
        maxw = 0
        for j in range(m):
            if j != i-1 and j != i:
                maxw = max(maxw, pld(p1, p2, s[j]))
        minw = min(minw, maxw)
    return minw


def pld(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    a = y2-y1
    b = x2-x1
    c = x1*a - y1*b
    return abs(-a*x3+b*y3+c)/((a*a+b*b)**0.5)


case = 1
while True:
    n = int(input())
    if not n:
        break

    p = []
    x0, y0 = int(1e9), 0
    for _ in range(n):
        x, y = map(int, input().split())
        if x0 > x:
            if x0 != int(1e9):
                p.append((x0, y0))
            x0, y0 = x, y
        elif x0 == x and y0 > y:
            p.append((x0, y0))
            x0, y0 = x, y
        else:
            p.append((x, y))

    p = asort(p)
    s = convex(p)
    print('Case {0:d}: {1:0.2f}'.format(case, math.ceil(width(s)*100)/100))
    case += 1
