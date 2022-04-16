import os
import io
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, k = map(int, input().split())
sn = (n+1)//int((n+1)**0.5)
arr = [*map(int, input().split())]
pre = [0]*(n+1)
for i in range(n):
    pre[i+1] = (pre[i]+arr[i]) % k
m = int(input())
qry = [[]for _ in range(sn+1)]
for i in range(m):
    a, b = map(int, input().split())
    qry[(a-1)//sn].append((a-1, b, i))


def insert_right(l, r):
    global right_result
    for x in range(l, r+1):
        y = pre[x]
        right_max[y] = x
        if update_turn[y] != update:
            update_turn[y] = update
            right_min[y] = x
        right_result = max(right_result, x - right_min[y])


def insert_left(l, r, result):
    left_max = {}
    for x in range(r, l-1, -1):
        y = pre[x]
        if y not in left_max:
            left_max[y] = right_max[y] if update_turn[y] == update else x
        result = max(result, left_max[y] - x)
    return result


right_max = [-1]*k
right_min = [-1]*k
update_turn = [-1]*k
update = 0
mid = 0

answer = [0]*m
for qry_set in qry:
    if not qry_set:
        continue
    right_result = 0
    qry_set.sort(key=lambda x: (x[1], x[0]))
    mid = min(mid+sn, n+1)
    li, lj = 0, mid-1

    for w in range(len(qry_set)):
        ni, nj, nk = qry_set[w]
        if nj < mid:
            answer[nk] = insert_left(ni, nj, right_result)
        else:
            insert_right(lj+1, nj)
            answer[nk] = insert_left(ni, mid-1, right_result)
        li, lj = ni, nj
    update += 1
for x in answer:
    print(x)
