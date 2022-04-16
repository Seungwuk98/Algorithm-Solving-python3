a = int(input())
tree = dict()
for _ in range(a):
    k, v1, v2 = input().split()
    if k not in tree:
        tree[k] = []
    tree[k].append(v1)
    tree[k].append(v2)


# def preorder(tree):
#     visited = []
#     queue = ['A']
#     while queue:
#         visit = queue.pop(0)
#         if visit == '.':
#             continue
#         queue.extend(tree[visit])
#         visited.append(visit)
#     return visited

# def DFS(tree):
#     visited = []
#     queue = ['A']
#     while queue:
#         visit = queue.pop(0)
#         queue.extend(tree[visit])
#         visited.append(visit)
#     return visited


def inorder(tree, node):
    left = tree[node][0]
    right = tree[node][1]
    if left == '.' and right == '.':
        print(node, end='')
        return
    if left != '.':
        inorder(tree, left)
    print(node, end='')
    if right != '.':
        inorder(tree, right)


def preorder(tree, node):
    left = tree[node][0]
    right = tree[node][1]
    if left == '.' and right == '.':
        print(node, end='')
        return
    print(node, end='')
    if left != '.':
        preorder(tree, left)
    if right != '.':
        preorder(tree, right)


def postorder(tree, node):
    left = tree[node][0]
    right = tree[node][1]
    if left == '.' and right == '.':
        print(node, end='')
        return
    if left != '.':
        postorder(tree, left)
    if right != '.':
        postorder(tree, right)
    print(node, end='')


preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')
