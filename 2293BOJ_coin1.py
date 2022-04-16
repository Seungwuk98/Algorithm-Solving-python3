import sys
input = sys.stdin.readline

n, k = map(int, input().split())
pre = [1000000]*(k+1)
pre[0] = 0
coin = [int(input())for _ in range(n)]
for x in coin:
    for y in range(x, k+1, 1):
        pre[y] = min(pre[y-x]+1, pre[y])
if pre[-1] == 1000000:
    print(-1)
else:
    print(pre[-1])
