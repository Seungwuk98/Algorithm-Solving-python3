from itertools import combinations

n, m = map(int, input().split())
mat = [[*map(int, input().split())]for _ in range(n)]


def cal_chicken_dist(x1, y1, x2, y2):
    return abs(x2-x1)+abs(y2-y1)


home = []
chicken = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            home.append((i, j))
        elif mat[i][j] == 2:
            chicken.append((i, j))

home_chicken_dist = [[]for _ in range(len(home))]
for i in range(len(home)):
    x1, y1 = home[i]
    for x2, y2 in chicken:
        home_chicken_dist[i].append(cal_chicken_dist(x1, y1, x2, y2))

city = 1e9
for i in range(1, m+1):
    chicken_comb = combinations(range(len(chicken)), i)
    for x in chicken_comb:
        r = 0
        for y in home_chicken_dist:
            dist = 1e9
            for idx in x:
                dist = min(dist, y[idx])
            r += dist
        city = min(city, r)

print(city)
