import os
import io
from bisect import bisect_left
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.parent = None
        self.key = key


class SplayTree:
    def __init__(self):
        self.root = None

    def rotate(self, node):
        parent = node.parent
        if not parent:
            return
        if parent.left == node:
            parent.left = x = node.right  # p의 왼쪽 자식에 노드의 오른쪽 자식을 넣고
            node.right = parent  # 노드의 오른쪽 자식이 p가 됨
        else:
            parent.right = x = node.left  # p의 오른쪽 자식에 노드의 왼쪽 자식을 넣고
            node.left = parent  # 노드의 왼쪽 자식이 p가 됨
        node.parent = parent.parent  # 노드의 부모는 p의 부모인 g가 되고
        parent.parent = node  # p의 부모는 노드가 됨
        if x:
            x.parent = parent  # 옮겨진 노드의 자식이 있다면, 그의 부모는 p가 됨
        if not node.parent:  # 만약 노드의 부모가 없다면 스스로 루트가 되고
            self.root = node
        elif node.parent.left == parent:  # 만약 g의 왼쪽 자식이 p였다면 노드가 g의 왼쪽자식이 되고
            node.parent.left = node
        else:  # 그 외에 경우에는 노드가 오른쪽 자식이 된다.
            node.parent.right = node

    def splay(self, node):
        while node.parent:
            parent = node.parent
            grand = parent.parent
            if grand:
                self.rotate(parent if (node == parent.left) ==
                            (parent == parent.left) else node)
            self.rotate(node)

    def insert(self, key):
        node = self.root
        if not node:
            self.root = Node(key)
            return
        while True:
            if key == node.key:
                return
            elif key < node.key:
                if not node.left:
                    x = node.left = Node(key)
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    x = node.right = Node(key)
                    break
                else:
                    node = node.right
        x.parent = node
        self.splay(x)

    def find(self, key):
        node = self.root
        if not node:
            return False
        while node:
            if key == node.key:
                break
            elif key < node.key:
                if not node.left:
                    break
                node = node.left
            else:
                if not node.right:
                    break
                node = node.right
        self.splay(node)
        return key == node.key

    def delete(self, key):
        if not self.find(key):
            return
        node = self.root
        if node.left:
            if node.right:
                self.root = node.left
                self.root.parent = None
                x = self.root
                while x.right:
                    x = x.right
                x.right = node.right
                node.right.parent = x
                self.splay(x)
                del node
                return
            self.root = node.left
            self.root.parent = None
            del node
            return
        elif node.right:
            self.root = node.right
            self.root.parent = None
            del node
            return
        else:
            del node
            self.root = None

    def find_max(self):
        node = self.root
        while node.right:
            node = node.right
        return node.key

    def find_min(self):
        node = self.root
        while node.left:
            node = node.left
        return node.key

    def lower_bound(self, key):
        node = self.root
        if not node:
            return None, None
        left, right = None, None
        while True:
            if key <= node.key:
                right = node
                if not node.left:
                    break
                node = node.left
            else:
                left = node
                if not node.right:
                    break
                node = node.right
        return left, right

    def upper_bound(self, key):
        node = self.root
        left, right = None, None
        while True:
            if key < node.key:
                right = node
                if not node.left:
                    break
                node = node.left
            else:
                left = node
                if not node.right:
                    break
                node = node.right
        return right


n = int(input())
h = {}
tree = SplayTree()
for _ in range(n):
    x = int(input())
    left, right = tree.lower_bound(x)
    m_h = 0
    if left:
        m_h = max(h[left.key], m_h)
    if right:
        m_h = max(h[right.key], m_h)
    tree.insert(x)
    h[x] = m_h+1
print(sum([*h.values()]))
