import os
import io
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m = map(int, input().split())


class Node:
    def __init__(self, lo, hi) -> None:
        self.sum = 0
        self.lo = lo
        self.hi = hi
        self.lazy = 0
        self.left = self.right = None


class SegTree:
    def __init__(self) -> None:
        self.root = self.init(1, n)

    def init(self, lo, hi):
        node = Node(lo, hi)
        if lo == hi:
            return node
        mid = lo + hi >> 1
        node.left = self.init(lo, mid)
        node.right = self.init(mid+1, hi)
        return node

    def prop(self, node):
        if not node.lazy:
            return
        node.sum = node.hi - node.lo + 1 - node.sum
        node.lazy = 0
        if node.left and node.right:
            node.left.lazy ^= 1
            node.right.lazy ^= 1

    def change(self, l, r):
        def do(node, l, r):
            if node.lo == l and node.hi == r:
                node.lazy ^= 1
                self.prop(node)
                return
            self.prop(node)
            mid = node.lo + node.hi >> 1
            if r <= mid:
                do(node.left, l, r)
                self.prop(node.right)
            elif l > mid:
                self.prop(node.left)
                do(node.right, l, r)
            else:
                do(node.left, l, mid)
                do(node.right, mid+1, r)
            node.sum = node.left.sum + node.right.sum
        do(self.root, l, r)

    def query(self, l, r):
        def do(node, l, r):
            self.prop(node)
            if node.lo == l and node.hi == r:
                return node.sum
            mid = node.lo + node.hi >> 1
            if r <= mid:
                self.prop(node.right)
                return do(node.left, l, r)
            elif l > mid:
                self.prop(node.left)
                return do(node.right, l, r)
            else:
                return do(node.left, l, mid) + do(node.right, mid+1, r)
        return do(self.root, l, r)


tree = SegTree()
for _ in range(m):
    q, a, b = map(int, input().split())
    if q:
        sys.stdout.write('{}\n'.format(tree.query(a, b)))
    else:
        tree.change(a, b)
