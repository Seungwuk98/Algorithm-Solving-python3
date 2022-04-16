import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        node = self.root
        while True:
            if data < node.data:
                if not node.left:
                    node.left = Node(data)
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = Node(data)
                    break
                else:
                    node = node.right

    def post_order(self, node):
        if not node.left and not node.right:
            print(node.data)
            return

        if node.left:
            self.post_order(node.left)
        if node.right:
            self.post_order(node.right)
        print(node.data)


root = int(input())
tree = Tree(root)
while True:
    try:
        tree.insert(int(input()))
    except:
        break

tree.post_order(tree.root)
