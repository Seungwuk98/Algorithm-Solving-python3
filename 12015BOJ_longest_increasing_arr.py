import sys
input = sys.stdin.readline
n = int(input())
arr = [*map(int, input().split())]
b = min(arr)
for i in range(n):
    arr[i] -= b-1
a = max(arr)
dp = [0]*(a+1)


def find_max(n):
    max_v = 0
    while n:
        max_v = max(dp[n], max_v)
        n -= n & -n
    return max_v


def update(n):
    max_v = find_max(n-1)
    while n < a+1:
        dp[n] = max(dp[n], max_v+1)
        n += n & -n


for i in arr:
    update(i)
print(find_max(a))
