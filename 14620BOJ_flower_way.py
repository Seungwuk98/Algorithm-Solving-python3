from itertools import combinations


def check(data):
    for i in range(2):
        for j in range(i+1, 3):
            if abs(data[i][0]-data[j][0])+abs(data[i][1]-data[j][1]) <= 2:
                return False
    return True


def cal_cost(data):
    r = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x, y in data:
        r += cost[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            r += cost[nx][ny]
    return r


n = int(input())
cost = [[*map(int, input().split())]for i in range(n)]
point = []

for i in range(1, n-1):
    for j in range(1, n-1):
        point.append((i, j))

comb = list(combinations(point, 3))
min_value = 1e6
for x in comb:
    if check(x):
        money = cal_cost(x)
        if money < min_value:
            min_value = money

print(min_value)
