from collections import deque
n, k = map(int, input().split())
level = {n: 0}
b = list()
a = deque([n])
while True:
    node = a.popleft()
    if node == k:
        print(level[node])
        break
    for i in (node-1, node+1, node*2):
        if i <= 100000 and i >= 0:
            if i not in level:
                level[i] = level[node]+1
                a.append(i)
