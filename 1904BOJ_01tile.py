a = int(input())
tileans = {1: 1, 2: 2, 3: 3}


def tile(a):
    if a == 1:
        return tileans[1]
    elif a == 2:
        return tileans[2]
    elif a == 3:
        return tileans[3]
    else:
        if a not in tileans.keys():
            tileans[a] = tile(a//2)*tile(a-a//2) + \
                tile(a//2-1) * tile(a-a//2-1)
            return tileans[a]
        else:
            return tileans[a]


print(tile(a) % 15746)
