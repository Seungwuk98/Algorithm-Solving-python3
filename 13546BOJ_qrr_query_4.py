import os
import io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


class Node:
    def __init__(self, key, item=None) -> None:
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.item = item


class SplayTree:
    def __init__(self):
        self.root = None
        self.max = None
        self.min = None

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

    def insert(self, key, item=None):
        node = self.root
        if not node:
            self.root = Node(key, item)
            self.min = key
            self.max = key
            return
        else:
            self.min = min(self.min, key)
            self.max = max(self.max, key)
        while True:
            if key == node.key:
                return
            elif key < node.key:
                if not node.left:
                    x = node.left = Node(key, item)
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    x = node.right = Node(key, item)
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
                if key == self.max:
                    self.max = self.find_max()
                elif key == self.min:
                    self.min = self.find_min()
                return
            self.root = node.left
            self.root.parent = None
            del node
            if key == self.max:
                self.max = self.find_max()
            elif key == self.min:
                self.min = self.find_min()
            return
        elif node.right:
            self.root = node.right
            self.root.parent = None
            del node
            if key == self.max:
                self.max = self.find_max()
            elif key == self.min:
                self.min = self.find_min()
            return
        else:
            del node
            self.min = None
            self.max = None
            self.root = None

    def insert_one(self, key):
        if not self.find(key):
            self.insert(key, 0)
        node = self.root
        node.item += 1

    def delete_one(self, key):
        if not self.find(key):
            return
        node = self.root
        node.item -= 1
        if not node.item:
            self.delete(key)

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


def insert(x):
    y = arr[x]
    l_m = None
    if mem_tree[y].root:
        l_m = mem_tree[y].max - mem_tree[y].min
    mem_tree[y].insert(x)
    n_m = mem_tree[y].max - mem_tree[y].min
    if l_m is not None:
        max_tree.delete_one(l_m)
    max_tree.insert_one(n_m)


def delete(x):
    y = arr[x]
    l_m = mem_tree[y].max - mem_tree[y].min
    mem_tree[y].delete(x)
    max_tree.delete_one(l_m)
    if mem_tree[y].root:
        max_tree.insert_one(mem_tree[y].max - mem_tree[y].min)


n, k = map(int, input().split())
sn = int(n**0.5)
arr = [*map(int, input().split())]
m = int(input())
qry = []
for i in range(m):
    a, b = map(int, input().split())
    qry.append((a-1, b-1, i))
qry.sort(key=lambda x: (x[0]//sn, x[1]))

mem_tree = [SplayTree()for _ in range(k+1)]
max_tree = SplayTree()

fl, fr, fk = qry[0]
for x in range(fl, fr+1):
    insert(x)
result = [0]*m
result[fk] = max_tree.max

for w in range(1, m):
    ll, lr, lk = qry[w-1]
    nl, nr, nk = qry[w]
    if ll//sn == nl//sn:
        for x in range(lr+1, nr+1):
            insert(x)
        if ll < nl:
            for x in range(ll, nl):
                delete(x)
        else:
            for x in range(nl, ll):
                insert(x)
    else:
        if lr < nr:
            for x in range(lr+1, nr+1):
                insert(x)
        else:
            for x in range(nr+1, lr+1):
                delete(x)
        for x in range(ll, nl):
            delete(x)
    result[nk] = max_tree.max

for x in result:
    print(x)
