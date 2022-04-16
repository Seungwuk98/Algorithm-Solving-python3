a = int(input())
tree = dict()
parent = {i: i for i in range(1, a+1)}
for _ in range(a):
    k, v1, v2 = map(int, input().split())
    if k not in tree:
        tree[k] = []
    tree[k].append(v1)
    tree[k].append(v2)
    parent[v1] = k
    parent[v2] = k


def find(node):
    while parent[node] != node:
        node = parent[node]
    return node


sorted_list = []
level_list = dict()


def inorder(tree, node, level):
    if level not in level_list:
        level_list[level] = []
    level_list[level].append(node)
    left = tree[node][0]
    right = tree[node][1]

    if left == -1 and right == -1:
        sorted_list.append(node)
        return
    if left != -1:
        inorder(tree, left, level+1)
    sorted_list.append(node)
    if right != -1:
        inorder(tree, right, level+1)


inorder(tree, find(1), 1)

result = []
for i in range(1, len(level_list.keys())+1):
    result.append(sorted_list.index(
        level_list[i][-1]) - sorted_list.index(level_list[i][0])+1)
max_level = result.index(max(result))
print(max_level+1, result[max_level])
