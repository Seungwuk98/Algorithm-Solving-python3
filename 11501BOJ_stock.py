import sys
import os
import io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def stock(arr, start, end):
    ret = 0
    while start < end:
        mx = 0
        midx = -1
        for i in range(end, start-1, -1):
            if i and arr[i] < arr[i-1]:
                end -= 1
            else:
                break
        for i in range(end, start-1, -1):
            if mx < arr[i]:
                mx = arr[i]
                midx = i
        for i in range(start, midx):
            ret += mx - arr[i]
        start = midx + 1
    return ret


for _ in range(int(input())):
    n = int(input())
    arr = [*map(int, input().split())]
    print(stock(arr, 0, n-1))
