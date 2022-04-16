a = int(input())
blocks = [[i, *map(int, input().split())]for i in range(1, a+1)]
blocks.append([0, 0, 0, 0])
blocks.sort(key=lambda x: x[3])
dp = [0]*(a+1)

for i in range(1, a+1):
    for j in range(i):
        if blocks[i][1] > blocks[j][1]:
            dp[i] = max(dp[i], dp[j]+blocks[i][2])

max_value = max(dp)
idx = a
result = []
while idx != 0:
    if dp[idx] == max_value:
        result.append(blocks[idx][0])
        max_value -= blocks[idx][2]
    idx -= 1

print(len(result))
result.reverse()
for _ in result:
    print(_)
