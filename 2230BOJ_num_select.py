import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted([int(input())for _ in range(n)])

result = int(1e10)
i, j = 0, 0
while j < n and i < n:
    if arr[j] - arr[i] < m:
        j += 1
    else:
        result = min(result, arr[j] - arr[i])
        i += 1
print(result)
