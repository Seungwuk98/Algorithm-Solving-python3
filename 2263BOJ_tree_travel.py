import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
in_order = input().split()
post_order = input().split()


# def make_tree(in_order, post_order):
#     if len(in_order) == 1:
#         return in_order
#     elif not in_order:
#         return [-1]
#     root = post_order[-1]
#     tree = {'value': root}
#     for i in range(n):
#         if in_order[i] == root:
#             root_idx = i
#             break
#     left_in_order = in_order[:i]
#     right_in_order = in_order[i+1:]
#     left_post_order = post_order[:i]
#     right_post_order = post_order[i:-1]

#     tree['left'] = make_tree(left_in_order, left_post_order)
#     tree['right'] = make_tree(right_in_order, right_post_order)
#     return tree


def pre(i_s, i_e, p_s, p_e):
    if i_s == i_e:
        return in_order[i_s]
    elif i_s > i_e:
        return None
    root = post_order[p_e]
    print(root, end=' ')
    i = in_order.index(root)
    lo_i = i-i_s
    left = pre(i_s, i-1, p_s, p_s+lo_i-1)
    if left:
        print(left, end=' ')
    right = pre(i+1, i_e, p_s+lo_i, p_e-1)
    if right:
        print(right, end=' ')


# tree = make_tree(in_order, post_order)
pre(0, n-1, 0, n-1)

# # def inorder(tree):
# #     if 'left' in tree or 'right' in tree:
# #         value = tree['value']
# #         if 'left' in tree:
# #             inorder(tree['left'])
# #         print(value, end=' ')
# #         if 'right' in tree:
# #             inorder(tree['right'])
# #     else:
# #         if tree[0] != -1:
# #             print(tree[0], end=' ')


# # def postorder(tree):
# #     if 'left' in tree or 'right' in tree:
# #         value = tree['value']
# #         if 'left' in tree:
# #             postorder(tree['left'])
# #         if 'right' in tree:
# #             postorder(tree['right'])
# #         print(value, end=' ')
# #     else:
# #         if tree[0] != -1:
# #             print(tree[0], end=' ')


# def preorder(tree):
#     if 'left' in tree or 'right' in tree:
#         value = tree['value']
#         print(value, end=' ')
#         if 'left' in tree:
#             preorder(tree['left'])
#         if 'right' in tree:
#             preorder(tree['right'])
#     else:
#         if tree[0] != -1:
#             print(tree[0], end=' ')


# preorder(tree)
