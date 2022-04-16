from collections import deque
from copy import *
import sys
input = sys.stdin.readline
n = int(input())
board = [[*map(int, input().split())]for _ in range(n)]


def dfs(data, level):
    if level == 5:
        return max_n(data)
    max_value = 0

    max_value = max(max_value, dfs(left(data), level+1))
    max_value = max(max_value, dfs(right(data), level+1))
    max_value = max(max_value, dfs(up(data), level+1))
    max_value = max(max_value, dfs(down(data), level+1))

    return max_value


def max_n(data):
    max_value = 0
    for x in data:
        max_value = max(max_value, max(x))
    return max_value


def up(data):
    u = deque([])
    v = []
    k = deepcopy(data)
    for j in range(n):
        for i in range(n):
            if k[i][j] != 0:
                if v and v[-1] == k[i][j]:
                    u.append(v.pop()*2)
                elif v:
                    u.append(v.pop())
                    v.append(k[i][j])
                else:
                    v.append(k[i][j])
        if v:
            u.append(v.pop())
        for i in range(n):
            if u:
                k[i][j] = u.popleft()
            else:
                k[i][j] = 0
    return k


def down(data):
    u = deque([])
    v = []
    k = deepcopy(data)
    for j in range(n):
        for i in range(n-1, -1, -1):
            if k[i][j] != 0:
                if v and v[-1] == k[i][j]:
                    u.append(v.pop()*2)
                elif v:
                    u.append(v.pop())
                    v.append(k[i][j])
                else:
                    v.append(k[i][j])
        if v:
            u.append(v.pop())
        for i in range(n-1, -1, -1):
            if u:
                k[i][j] = u.popleft()
            else:
                k[i][j] = 0
    return k


def left(data):
    u = deque([])
    v = []
    k = deepcopy(data)
    for i in range(n):
        for j in range(n):
            if k[i][j] != 0:
                if v and v[-1] == k[i][j]:
                    u.append(v.pop()*2)
                elif v:
                    u.append(v.pop())
                    v.append(k[i][j])
                else:
                    v.append(k[i][j])

        if v:
            u.append(v.pop())
        for j in range(n):
            if u:
                k[i][j] = u.popleft()
            else:
                k[i][j] = 0
    return k


def right(data):
    u = deque([])
    v = []
    k = deepcopy(data)
    for i in range(n):
        for j in range(n-1, -1, -1):
            if k[i][j] != 0:
                if v and v[-1] == k[i][j]:
                    u.append(v.pop()*2)
                elif v:
                    u.append(v.pop())
                    v.append(k[i][j])
                else:
                    v.append(k[i][j])
        if v:
            u.append(v.pop())
        for j in range(n-1, -1, -1):
            if u:
                k[i][j] = u.popleft()
            else:
                k[i][j] = 0
    return k


print(dfs(board, 0))
