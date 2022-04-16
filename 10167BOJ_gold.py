import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
point = [()for _ in range(n)]
x_sort = set()
y_sort = set()
for i in range(n):
    x, y, w = map(int, input().split())
    x_sort.add(x)
    y_sort.add(y)
    point[i] = (x, y, w)
x_sort = sorted([*x_sort])
y_sort = sorted([*y_sort])
for i in range(n):
    x, y, w = point[i]
    point[i] = (bisect_left(x_sort, x), bisect_left(y_sort, y), w)
point.sort(key=lambda x: x[1])


class Node:
    def __init__(self, lo, hi) -> None:
        self.lo = lo
        self.hi = hi
        self.lmax = self.rmax = self.max = self.sum = 0
        self.left = self.right = None


class SegTree:
    def __init__(self) -> None:
        self.root = self.init(0, 3000)

    def init(self, lo, hi):
        node = Node(lo, hi)
        if lo == hi:
            return node
        mid = lo + hi >> 1
        node.left = self.init(lo, mid)
        node.right = self.init(mid+1, hi)
        return node

    def reset(self, node):
        node.lmax = node.rmax = node.max = node.sum = 0
        if node.lo == node.hi:
            return
        self.reset(node.left)
        self.reset(node.right)

    def update(self, node, x, w):
        if node.lo == node.hi:
            node.sum += w
            node.lmax = node.rmax = node.max = node.sum
            return
        mid = node.lo + node.hi >> 1
        self.update(node.left if x <= mid else node.right, x, w)
        node.sum = node.left.sum + node.right.sum
        node.lmax = node.left.lmax if node.left.lmax > node.left.sum + \
            node.right.lmax else node.left.sum + node.right.lmax
        node.rmax = node.right.rmax if node.right.rmax > node.right.sum + \
            node.left.rmax else node.right.sum + node.left.rmax
        node.max = max(node.left.max, node.right.max,
                       node.left.rmax + node.right.lmax)


result = 0
tree = SegTree()
for i in range(n):
    if i and point[i-1][1] == point[i][1]:
        continue
    tree.reset(tree.root)
    for j in range(i, n):
        tree.update(tree.root, point[j][0], point[j][2])
        if j == n-1 or point[j][1] != point[j+1][1]:
            result = max(result, tree.root.max)
print(result)
