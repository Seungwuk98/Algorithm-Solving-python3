import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [int(input())for _ in range(n)]


class Node:
    def __init__(self, data, bottom, up) -> None:
        self.data = data
        self.bottom = bottom
        self.up = up
        self.mid = (bottom+up)//2
        self.left = None
        self.right = None
        self.lazy = 0


class SegTree:
    def __init__(self) -> None:
        length = len(arr)
        self.root = self.init(0, length-1)

    def init(self, bottom, up):
        if bottom == up:
            return Node(arr[bottom], up, up)

        node = Node(None, bottom, up)
        mid = node.mid
        node.left = self.init(bottom, mid)
        node.right = self.init(mid+1, up)
        node.data = node.left.data + node.right.data
        return node

    def update_ord(self, b, c, d):
        b -= 1
        c -= 1
        if b > c:
            b, c = c, b
        self.update(self.root, b, c, d)

    def update(self, node, b, c, d):
        if node.bottom == b and node.up == c:
            node.data += d*(c-b+1)
            node.lazy += d
            return

        node.data += d*(c-b+1)
        if c <= node.mid:
            self.update(node.left, b, c, d)
        elif b > node.mid:
            self.update(node.right, b, c, d)
        else:
            self.update(node.left, b, node.mid, d)
            self.update(node.right, node.mid+1, c, d)

    def qry(self, b, c):
        b -= 1
        c -= 1
        if b > c:
            b, c = c, b
        return self.find(self.root, b, c)

    def find(self, node, b, c):
        if node.bottom == b and node.up == c:
            return node.data

        self.prop(node)

        left = right = 0
        if c <= node.mid:
            left = self.find(node.left, b, c)
        elif b > node.mid:
            right = self.find(node.right, b, c)
        else:
            left = self.find(node.left, b, node.mid)
            right = self.find(node.right, node.mid+1, c)
        return left+right

    def prop(self, node):
        if node.lazy and node.left and node.right:
            node.left.data += (node.mid - node.bottom + 1)*node.lazy
            node.right.data += (node.up - node.mid)*node.lazy
            node.left.lazy += node.lazy
            node.right.lazy += node.lazy
            node.lazy = 0


tree = SegTree()

for _ in range(m+k):
    qry = [*map(int, input().split())]
    if qry[0] == 1:
        tree.update_ord(qry[1], qry[2], qry[3])
    else:
        print(tree.qry(qry[1], qry[2]))
