from pprint import pprint
n = int(input())
arr = [*map(int, input().split())]
length = len(arr)
dp = [0]*length
for i in range(0, length):
    dp[i] = arr[i]
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])
print(max(dp))
