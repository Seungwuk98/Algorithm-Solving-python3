n = int(input())
arr = sorted([int(input())for _ in range(n)])
b = set([x+y for x in arr for y in arr])
for i in range(n-1, 0, -1):
    for j in range(i):
        if arr[i]-arr[j] in b:
            print(arr[i])
            exit(0)
