import sys
input = sys.stdin.readline


class Node:
    def __init__(self, low, up, _min, _max) -> None:
        self.low = low
        self.up = up
        self.min = _min
        self.mid = (low+up)//2
        self.max = _max
        self.left = None
        self.right = None


class SegTree:
    def __init__(self, n, data) -> None:
        self.root = Node(1, 2**n, min(data), max(data))
        self.root.left = self.makeTree(1, 2**(n-1), data)
        self.root.right = self.makeTree(2**(n-1)+1, 2**n, data)

    def makeTree(self, low, up, data):
        if low == up:
            return Node(low, up, data[low-1], data[low-1])

        node = Node(low, up, min(data[low-1:up]), max(data[low-1:up]))
        mid = (low+up)//2
        node.left = self.makeTree(low, mid, data)
        node.right = self.makeTree(mid+1, up, data)
        return node

    def min_max(self, a, b):
        node = self.root

        def find_min_max(node, a, b):
            if node.low == a and node.up == b:
                return node.min, node.max
            elif node.mid >= a and node.mid >= b:
                return find_min_max(node.left, a, b)
            elif node.mid < a and node.mid < b:
                return find_min_max(node.right, a, b)
            else:
                left_min, left_max = find_min_max(node.left, a, node.mid)
                right_min, right_max = find_min_max(
                    node.right, node.mid+1, b)
                return min(left_min, right_min), max(left_max, right_max)

        return find_min_max(node, a, b)


n, m = map(int, input().split())
arr = [int(input())for _ in range(n)]

size = 1
count = 0
while size <= n:
    size *= 2
    count += 1
count += 1
size *= 2
left_size = size - n
arr += [-1e9]*left_size

tree = SegTree(count, arr)

for _ in range(m):
    a, b = map(int, input().split())
    print(*tree.min_max(a, b))
