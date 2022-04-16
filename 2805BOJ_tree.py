n, m = map(int, input().split())
trees = [*map(int, input().split())]
_min = 0
_max = max(trees)


def availabe(now, trees):
    sum = 0
    for i in trees:
        sum += i-now if i-now > 0 else 0

    if sum < m:
        return False
    else:
        return True


while _max > _min:
    now = (_max+_min)//2+1
    if availabe(now, trees):
        _min = now
    else:
        _max = now - 1

print(_min)
