k, n = map(int, input().split())
lan = [int(input())for _ in range(k)]
_max = max(lan)
_min = 1


def available(now, lan, n):
    sum = 0
    for i in lan:
        sum += i//now
    if sum < n:
        return False
    else:
        return True


while _max > _min:
    now = (_max+_min)//2+1
    if available(now, lan, n):
        _min = now
    else:
        _max = now-1

print(_min)
