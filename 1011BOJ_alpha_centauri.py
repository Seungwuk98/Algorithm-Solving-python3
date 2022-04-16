from collections import deque


def sum(n):
    return n*(n+1)//2


for _ in range(int(input())):
    x, y = map(int, input().split())
    r = 1e10
    interval = y-x
    k = 1
    while sum(k)+sum(k+1) <= interval:
        k += 1
    left = interval-sum(k)-sum(k-1)
    if left > k:
        print(2*k+1)
    elif 0 < left <= k:
        print(2*k)
    else:
        print(2*k-1)
