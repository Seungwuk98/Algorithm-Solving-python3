from heapq import *
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
p = []
x0, y0 = [int(1e9)]*2
for _ in range(n):
    a, b = map(int, input().split())
    if a < x0:
        if (x0, y0) != (int(1e9), int(1e9)):
            p.append((x0, y0))
        x0, y0 = a, b
    elif a == x0 and b < y0:
        p.append((x0, y0))
        y0 = b
    else:
        p.append((a, b))


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)


def compare(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    c = ccw(x0, y0, x1, y1, x2, y2)
    if not c:
        if x1 == x2:
            return y1 > y2
        else:
            return x1 > x2
    else:
        return c < 0


def qsort(p):
    if len(p) <= 1:
        return p
    pivot = p[0]
    left = [x for x in p[1:] if compare(pivot, x)]
    right = [x for x in p[1:] if not compare(pivot, x)]
    return qsort(left) + [pivot] + qsort(right)


p = qsort(p)
s = [(x0, y0), p[0]]
i = 1
while i < n-1:
    if len(s) <= 1:
        s.append(p[i])
        i += 1
    else:
        c = ccw(*s[-2], *s[-1], *p[i])
        if c <= 0:
            s.pop()
            continue
        s.append(p[i])
        i += 1

if not ccw(*s[-2], *s[-1], x0, y0):
    s.pop()

print(len(s))
