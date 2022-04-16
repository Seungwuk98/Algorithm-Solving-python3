import os
import io
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
arr = [*map(int, input().split())]


class Node:
    def __init__(self, bottom, up) -> None:
        self.data = 0
        self.bottom = bottom
        self.up = up
        self.mid = (bottom + up) // 2
        self.lazy = 0
        self.left = None
        self.right = None


class SegTree:
    def __init__(self) -> None:
        self.root = self.init(0, n-1)

    def init(self, bottom, up):
        node = Node(bottom, up)
        if bottom == up:
            node.data = arr[up]
            return node
        mid = node.mid
        node.left = self.init(bottom, mid)
        node.right = self.init(mid+1, up)
        node.data = node.left.data ^ node.right.data
        return node

    def update(self, l, r, val):
        self.do_update(self.root, l, r, val)

    def do_update(self, node, l, r, val):
        if node.bottom == l and node.up == r:
            node.lazy ^= val
            return
        c = r-l+1
        if c & 1:
            node.data ^= val
        if r <= node.mid:
            self.do_update(node.left, l, r, val)
        elif l > node.mid:
            self.do_update(node.right, l, r, val)
        else:
            self.do_update(node.left, l, node.mid, val)
            self.do_update(node.right, node.mid+1, r, val)

    def find(self, l, r):
        return self.do_find(self.root, l, r)

    def do_find(self, node, l, r):
        if node.lazy:
            self.prop(node)
        if node.bottom == l and node.up == r:
            return node.data

        left = right = 0
        if r <= node.mid:
            left = self.do_find(node.left, l, r)
        elif l > node.mid:
            right = self.do_find(node.right, l, r)
        else:
            left = self.do_find(node.left, l, node.mid)
            right = self.do_find(node.right, node.mid+1, r)
        return left ^ right

    def prop(self, node):
        c = node.up - node.bottom + 1
        if c & 1:
            node.data ^= node.lazy

        if node.left:
            node.left.lazy ^= node.lazy
        if node.right:
            node.right.lazy ^= node.lazy
        node.lazy = 0


tree = SegTree()

for _ in range(int(input())):
    qry = [*map(int, input().split())]
    if qry[0] == 1:
        tree.update(qry[1], qry[2], qry[3])
    else:
        sys.stdout.write('{}\n'.format(tree.find(qry[1], qry[2])))
