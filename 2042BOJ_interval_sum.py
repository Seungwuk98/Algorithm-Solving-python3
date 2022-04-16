import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [int(input())for _ in range(n)]
bit = [0]*(n+1)

for i in range(1, n+1):
    for j in range(i-(i & -i), i):
        bit[i] += arr[j]


def update(b, c):
    tmp = arr[b-1]
    arr[b-1] = c
    t = b
    while t <= n:
        bit[t] += -tmp+c
        t += t & -t


def seqsum(b):
    r = 0
    t = b
    while t > 0:
        r += bit[t]
        t -= t & -t
    return r


for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    else:
        print(seqsum(c)-seqsum(b-1))
