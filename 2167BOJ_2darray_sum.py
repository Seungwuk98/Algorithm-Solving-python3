import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0]+[*map(int, input().split())]for _ in range(n)]
for x in arr:
    for j in range(1, m+1):
        x[j] = x[j-1] + x[j]
for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    sum_v = 0
    for k in range(i-1, x):
        sum_v += arr[k][y] - arr[k][j-1]
    print(sum_v)
