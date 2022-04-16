from bisect import bisect_left as bl
import sys
input = sys.stdin.readline


class Node:
    def __init__(self, lo, hi) -> None:
        self.lo = lo
        self.hi = hi
        self.cnt = 0
        self.l = self.r = None


class PST:
    def __init__(self, n) -> None:
        self.tree = [None]*(n+1)
        self.len = n
        self.tree[0] = self.init(0, n)

    def init(self, lo, hi):
        x = Node(lo, hi)
        if lo == hi:
            return x
        mid = lo + hi >> 1
        x.l = self.init(lo, mid)
        x.r = self.init(mid+1, hi)
        return x

    def update(self, i, z):
        if not self.tree[i]:
            self.tree[i] = Node(0, self.len)

        def do(p, x):
            if x.lo == x.hi:
                x.cnt += 1
                return
            mid = x.lo + x.hi >> 1
            if z <= mid:
                if not x.l:
                    x.l = Node(x.lo, mid)
                if not x.r:
                    x.r = p.r
                do(p.l, x.l)
            else:
                if not x.l:
                    x.l = p.l
                if not x.r:
                    x.r = Node(mid+1, x.hi)
                do(p.r, x.r)
            x.cnt = x.l.cnt + x.r.cnt
        do(self.tree[i-1], self.tree[i])

    def query(self, u, d, l, r):
        def do(up, dn, l, r):
            if dn.lo == l and dn.hi == r:
                return dn.cnt - up.cnt
            mid = dn.lo + dn.hi >> 1
            if r <= mid:
                return do(up.l, dn.l, l, r)
            elif l > mid:
                return do(up.r, dn.r, l, r)
            else:
                return do(up.l, dn.l, l, mid) + do(up.r, dn.r, mid+1, r)
        return do(self.tree[u-1], self.tree[d], l, r)


for _ in range(int(input())):
    p = []
    x_s = []
    y_s = []
    n, m = map(int, input().split())
    for __ in range(n):
        x, y = map(int, input().split())
        x_s.append(x)
        y_s.append(y)
        p.append([x, y])
    x_s.sort()
    y_s.sort()
    for i in range(n):
        p[i][0] = bl(x_s, p[i][0])+1
        p[i][1] = bl(y_s, p[i][1])+1
    p.sort()
    pst = PST(n)
    for x, y in p:
        pst.update(x, y)

    ret = 0
    for __ in range(m):
        u, d, l, r = map(int, input().split())
        u = bl(x_s, u)+1
        d = bl(x_s, d)+1
        l = bl(y_s, l)+1
        r = bl(y_s, r)+1
        ret += pst.query(u, d, l, r)
    print(ret)
