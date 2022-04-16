from re import X
import sys
input = sys.stdin.readline

n = map(int, input().split())
arr = [*map(int, input().split())]


class Node:
    def __init__(self) -> None:
        self.left = self.right = None
        self.max = self.smax = self.sum = 0
        self.maxcnt = 0


class Segtree:
    def __init__(self) -> None:
        self.tree = self.init(1, n)

    def init(self, lo, hi):
        x = Node()
        if lo == hi:
            x.max = x.sum = arr[lo-1]
            x.smax = 0
            return x
        mid = lo + hi >> 1
        x.left = self.init(lo, mid)
        x.right = self.init(mid+1, hi)
        if x.left.max < x.right.max:
            x.max = x.right.max
            x.smax = max(x.right.smax, x.left.max, x.left.smax)
            x.maxcnt = x.right.maxcnt
        elif x.left.max > x.right.max:
            x.max = x.left.max
            x.smax = max(x.right.max, x.right.smax, x.left.smax)
            x.maxcnt = x.left.maxcnt
        else:
            x.max = x.left.max
            x.smax = max(x.right.smax, x.left.smax)
            x.maxcnt = x.left.maxcnt + x.right.maxcnt
        x.sum = x.left.sum + x.right.sum
        return x

    def update(self, l, r, z):
        pass

    def prop(self, x):
        pass
