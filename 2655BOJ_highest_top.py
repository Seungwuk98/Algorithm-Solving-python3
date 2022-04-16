import copy

a = int(input())
b = {i: [*map(int, input().split())] for i in range(1, a+1)}
c = list(b.items())
c.sort(key=lambda x: x[1][0])


dp = [[[c[i][1][1], c[i][0]] for i in range(a)] for j in range(a+1)]


def available(small, big):
    if b[small][2] < b[big][2]:
        return True
    else:
        return False


max = 0
max_idx = [0, 0]
for i in range(1, a+1):
    for j in range(a):
        max_value = dp[i][j][0]
        for k in range(i):
            if available(dp[k][j][-1], c[i-1][0]):
                if dp[k][j][0]+c[i-1][1][1] > max_value:
                    tmp = copy.deepcopy(dp[k][j])
                    tmp.append(c[i-1][0])
                    tmp[0] = dp[k][j][0]+c[i-1][1][1]
                    dp[i][j] = tmp
                    if tmp[0] > max:
                        max = tmp[0]
                        max_idx = [i, j]

print(dp[i][j])
