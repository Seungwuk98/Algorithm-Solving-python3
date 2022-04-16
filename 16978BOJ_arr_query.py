import os
import io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
arr = [*map(int, input().split())]
bit = [0]*(n+1)
for i in range(1, n+1):
    x = i & -i
    bit[i] = sum(arr[i-x:i])


def update(i, v):
    t = arr[i-1]
    arr[i-1] = v
    d = v-t
    while i <= n:
        bit[i] += d
        i += i & -i


def query():
    while qry2 and qry2[-1][1] == num:
        r = 0
        x, y, l, m, k = qry2.pop()
        l -= 1
        while m:
            r += bit[m]
            m -= m & -m
        while l:
            r -= bit[l]
            l -= l & -l
        result[k] = r


qry1 = []
qry2 = []
r = 0
for _ in range(int(input())):
    qry = [*map(int, input().split())]
    if qry[0] == 1:
        qry1.append(qry)
    else:
        qry.append(r)
        qry2.append(qry)
        r += 1
qry2.sort(reverse=True)
result = [0]*(len(qry2))
num = 0
for x, i, v in qry1:
    query()
    update(i, v)
    num += 1
query()
print('\n'.join(map(str, result)))
