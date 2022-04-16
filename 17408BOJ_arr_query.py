import os
import io
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
arr = [*map(int, input().split())]


class Node:
    def __init__(self, bottom, up) -> None:
        self.data1 = 0
        self.data2 = 0
        self.bottom = bottom
        self.up = up
        self.mid = (bottom + up)//2
        self.left = self.right = None


class SegTree:
    def __init__(self) -> None:
        self.root = self.init(1, n)

    def init(self, bottom, up):
        node = Node(bottom, up)
        if bottom == up:
            node.data1 = arr[up-1]
            return node
        mid = node.mid
        node.left = self.init(bottom, mid)
        node.right = self.init(mid+1, up)
        tmp = sorted([node.left.data1, node.left.data2,
                     node.right.data1, node.right.data2])
        node.data1 = tmp.pop()
        node.data2 = tmp.pop()
        return node

    def update(self, i, v):
        self.do_update(self.root, i, v)

    def do_update(self, node, i, v):
        if node.bottom == node.up:
            node.data1 = v
            return

        if i <= node.mid:
            self.do_update(node.left, i, v)
        else:
            self.do_update(node.right, i, v)

        tmp = sorted([node.left.data1, node.left.data2,
                     node.right.data1, node.right.data2])
        node.data1 = tmp.pop()
        node.data2 = tmp.pop()

    def find(self, l, r):
        data1, data2 = self.do_find(self.root, l, r)
        return data1 + data2

    def do_find(self, node, l, r):
        if node.bottom == l and node.up == r:
            return node.data1, node.data2

        left1 = left2 = right1 = right2 = 0
        if r <= node.mid:
            left1, left2 = self.do_find(node.left, l, r)
        elif l > node.mid:
            right1, right2 = self.do_find(node.right, l, r)
        else:
            left1, left2 = self.do_find(node.left, l, node.mid)
            right1, right2 = self.do_find(node.right, node.mid+1, r)
        tmp = sorted([left1, left2, right1, right2])
        data1 = tmp.pop()
        data2 = tmp.pop()
        return data1, data2


tree = SegTree()
for _ in range(int(input())):
    q, a, b = map(int, input().split())
    if q == 1:
        tree.update(a, b)
    else:
        sys.stdout.write('{}\n'.format(tree.find(a, b)))
