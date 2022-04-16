n, l, k = map(int, input().split())
pr = [[*map(int, input().split())]for _ in range(n)]
result = 0
count1 = 0
count2 = 0
for i, j in pr:
    if l >= i:
        result += 100
        count1 += 1
    if l >= j:
        result += 40
        count2 += 1
result -= 100*max(count1-max(count2, k), 0) + 140*max(count2-k, 0)
print(result)
