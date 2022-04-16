import sys
input = sys.stdin.readline
n = int(input())
arr = [*map(int, input().split())]
m = int(input())
dp = [[False]*n for _ in range(n)]
update = [[False]*n for _ in range(n)]


def felindrom(i, j):
    x, y = i-1, j-1
    update[i-1][j-1] = True
    c = True
    while x < y:
        if arr[x] != arr[y]:
            c = False
            break
        x += 1
        y -= 1
    dp[i-1][j-1] = c


for _ in range(m):
    s, e = map(int, input().split())
    if update[s-1][e-1]:
        print(+dp[s-1][e-1])
    else:
        felindrom(s, e)
        print(+dp[s-1][e-1])
