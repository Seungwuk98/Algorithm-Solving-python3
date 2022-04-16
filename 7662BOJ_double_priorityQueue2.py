import sys
input = sys.stdin.readline
INF = (1 << 31)-1
MINF = -(1 << 31)


class Node:
    def __init__(self) -> None:
        self.cnt = 0
        self.left = self.right = None


def init(x, s, e):
    x.cnt = 0
    if s == e:
        return
    mid = s + e >> 1
    if x.left:
        init(x.left, s, mid)
    if x.right:
        init(x.right, mid+1, e)


def update(x, s, e, w):
    if s == e:
        x.cnt += 1
        return
    mid = s+e >> 1
    if w <= mid:
        if not x.left:
            x.left = Node()
        update(x.left, s, mid, w)
    else:
        if not x.right:
            x.right = Node()
        update(x.right, mid+1, e, w)
    x.cnt = (x.left.cnt if x.left else 0) + (x.right.cnt if x.right else 0)


def kth_pop(x, s, e, k):
    if s == e:
        x.cnt -= 1
        return s
    diff = x.left.cnt if x.left else 0
    mid = s + e >> 1
    if k > diff:
        ret = kth_pop(x.right, mid+1, e, k-diff)
    else:
        ret = kth_pop(x.left, s, mid, k)
    x.cnt = (x.left.cnt if x.left else 0) + (x.right.cnt if x.right else 0)
    return ret


root = Node()
for _ in range(int(input())):
    init(root, MINF, INF)
    for __ in range(int(input())):
        qry = input().split()
        qry[1] = int(qry[1])
        if qry[0] == 'I':
            update(root, MINF, INF, qry[1])
        elif root.cnt:
            kth_pop(root, MINF, INF, root.cnt if qry[1] == 1 else 1)
    if not root.cnt:
        print('EMPTY')
    elif root.cnt == 1:
        x = kth_pop(root, MINF, INF, 1)
        print(x, x)
    else:
        print(kth_pop(root, MINF, INF, root.cnt), kth_pop(root, MINF, INF, 1))
