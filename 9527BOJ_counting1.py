def count(i, x):
    if x == 0:
        return 0, 0
    if x == 1:
        if i:
            return 1, (1 << (i-1))*i+1
        else:
            return 0, 1
    next, result = count(i+1, x >> 1)
    if x & 1:
        if i:
            result += (1 << (i-1))*i+1 + next*(1 << i)
        else:
            result += next+1
        return next+1, result
    else:
        return next, result


a, b = map(int, input().split())
z, x = count(0, a-1)
z, y = count(0, b)
print(y-x)
