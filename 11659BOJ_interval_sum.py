import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0]+[*map(int, input().split())]
for i in range(1, n+1):
    arr[i] += arr[i-1]
for _ in range(m):
    i, j = map(int, input().split())
    print(arr[j]-arr[i-1])
