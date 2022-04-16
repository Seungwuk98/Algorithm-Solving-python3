n, m, b = map(int, input().split())
ground = [[*map(int, input().split())]for _ in range(n)]
_min = min([min(x)for x in ground])
_max = max([max(x)for x in ground])


def need(now, ground):
    sum1 = 0
    sum2 = 0
    for i in range(n):
        for j in range(m):
            if now-ground[i][j] >= 0:
                sum1 += now - ground[i][j]
            else:
                sum2 += (ground[i][j] - now)*2
    return sum1+sum2, sum1-sum2//2


min_value, block = need(_min, ground)
for i in range(_min+1, _max+2):
    cost, block = need(i, ground)
    if cost > min_value or block > b:
        break
    else:
        min_value = cost

print(min_value, i-1)
