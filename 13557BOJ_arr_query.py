import sys
input = sys.stdin.readline
def print(x): return sys.stdout.write('{}\n'.format(x))


n = int(input())
arr = [*map(int, input().split())]


class Node:
    def __init__(self, lo, hi) -> None:
        self.lmax = self.max = self.rmax = self.sum = 0
        self.lo = lo
        self.hi = hi
        self.left = self.right = None


class SegTree:
    def __init__(self) -> None:
        self.tree = self.init(1, n)

    def init(self, lo, hi):
        node = Node(lo, hi)
        if lo == hi:
            node.lmax = node.rmax = node.max = node.sum = arr[lo-1]
            return node
        mid = lo + hi >> 1
        node.left = self.init(lo, mid)
        node.right = self.init(mid+1, hi)

        node.sum = node.left.sum + node.right.sum
        node.lmax = max(node.left.lmax, node.left.sum + node.right.lmax)
        node.rmax = max(node.right.rmax, node.right.sum + node.left.rmax)
        node.max = max(node.left.max, node.right.max,
                       node.left.rmax + node.right.lmax)

        return node

    def query(self, l, r):
        if l > r:
            return 0, 0, 0, 0

        def do(node, l, r):
            if node.lo == l and node.hi == r:
                return node.sum, node.lmax, node.rmax, node.max
            mid = node.lo + node.hi >> 1
            if r <= mid:
                return do(node.left, l, r)
            elif l > mid:
                return do(node.right, l, r)
            else:
                left = do(node.left, l, mid)
                right = do(node.right, mid+1, r)
                _sum = left[0] + right[0]
                lmax = max(left[1], left[0] + right[1])
                rmax = max(right[2], right[0] + left[2])
                _max = max(left[2] + right[1], left[3], right[3])
                return _sum, lmax, rmax, _max
        return do(self.tree, l, r)


tree = SegTree()

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    if x2 <= y1:
        left = tree.query(x1, x2-1)
        mid = tree.query(x2, y1)
        right = tree.query(y1+1, y2)
        # print((x1, x2), (x2+1, y1-1), (y1, y2))
        # print(left, mid, right)
        print(max(mid[3], left[2] + mid[1],
                  mid[2] + right[1], left[2] + mid[0] + right[1]))
    else:
        left = tree.query(x1, y1)
        mid = tree.query(y1+1, x2-1)
        right = tree.query(x2, y2)
        # print((x1, y1), (y1+1, x2-1), (x2, y2))
        # print(left, mid, right)
        print(left[2] + mid[0] + right[1])
    # print()
