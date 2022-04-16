from math import *
from itertools import combinations
import sys


def bisect_right(arr, v, key=lambda x: x):
    bottom, up = 0, len(arr)
    while bottom < up:
        mid = (bottom+up)//2
        if key(arr[mid]) <= v:
            bottom = mid+1
        else:
            up = mid
    return up


def bisect_left(arr, v, key=lambda x: x):
    bottom, up = 0, len(arr)
    while bottom < up:
        mid = (bottom+up)//2
        if key(arr[mid]) >= v:
            up = mid
        else:
            bottom = mid+1
    return up


def dist(x1, y1, x2, y2):
    return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)


input = sys.stdin.readline
n = int(input())
INF = int(1e9)
d = INF
arr = sorted([[*map(int, input().split())]for _ in range(n)])
def s_x(x): return x[0]
def s_y(y): return y[1]


def find(arr):
    global d
    l = len(arr)
    if not d:
        print(0)
        exit(0)

    if l <= 3:
        a_comb = combinations(arr, 2)
        for p1, p2 in a_comb:
            d = min(d, dist(*p1, *p2))
        return

    mid = l//2
    find(arr[:mid])
    find(arr[mid:])
    left = bisect_left(arr, arr[mid-1][0]-int(sqrt(d)+0.5), key=s_x)
    right = bisect_right(arr, arr[mid-1][0]+int(sqrt(d)+0.5), key=s_x)
    if left >= n or right <= 0:
        return

    l_p = sorted(arr[left:mid], key=s_y)
    r_p = sorted(arr[mid:right], key=s_y)
    for lx, ly in l_p:
        down = bisect_left(r_p, ly-int(sqrt(d)+0.5), key=s_y)
        up = bisect_right(r_p, ly+int(sqrt(d)+0.5), key=s_y)
        if down >= len(r_p) or up <= 0:
            continue
        for rx, ry in r_p[down:up]:
            d = min(d, dist(lx, ly, rx, ry))


find(arr)
print(d)
