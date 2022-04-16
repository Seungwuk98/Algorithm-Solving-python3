class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.child = {}


class Trie:
    def __init__(self) -> None:
        self.root = Node(None)

    def insert(self, arr):
        node = self.root
        for now in arr:
            if now not in node.child:
                node.child[now] = Node(now)
            node = node.child[now]

    def dfs(self, node, level):
        if node != self.root:
            print(level+node.data)
        key = sorted([*node.child.keys()])
        for x in key:
            self.dfs(node.child[x], level+('--' if node != self.root else ''))


data = []
for _ in range(int(input())):
    data.append([*input().split()][1:])
trie = Trie()
for x in data:
    trie.insert(x)
trie.dfs(trie.root, '')
