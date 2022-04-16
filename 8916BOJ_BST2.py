import sys
input = sys.stdin.readline


d = 9999991


def pow(c, n):
    r = 1
    while n:
        if n & 1:
            r = r*c % d
        c = c*c % d
        n >>= 1
    return r


def comb(n, r):
    l, s, t = 1, 1, 1
    for i in range(2, n+1):
        l = l*i % d
        if r == i:
            s = pow(l, d-2)
        if i == n-r:
            t = pow(l, d-2)
    return l*s % d*t % d


class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None
        self.comb = 0

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return
        node = self.root
        while True:
            if key == node.key:
                return
            elif key < node.key:
                if not node.left:
                    node.left = Node(key)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(key)
                    return
                node = node.right

    def find(self):
        self.comb = 1
        self.com(self.root)

    def com(self, node):
        left = 0
        right = 0
        if node.left:
            left = self.com(node.left)
        if node.right:
            right = self.com(node.right)
        self.comb = self.comb * comb(left+right, left) % d
        return left+right+1


for _ in range(int(input())):
    n = int(input())
    tree = BST()
    for x in map(int, input().split()):
        tree.insert(x)
    tree.find()
    print(tree.comb)
