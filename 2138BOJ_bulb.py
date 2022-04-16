n = int(input())
now = [int(x) for x in input()]
ret = [int(x) for x in input()]


def chk(now, ret):
    cnt = 0
    for i in range(1, n):
        if now[i-1] != ret[i-1]:
            now[i-1] ^= 1
            now[i] ^= 1
            if i + 1 < n:
                now[i+1] ^= 1
            cnt += 1
    if now[-1] != ret[-1]:
        return 1000000
    return cnt


result = 1000000
result = min(result, chk(now[::1], ret))
now[0] ^= 1
now[1] ^= 1
result = min(result, chk(now, ret)+1)
if result == 1000000:
    print(-1)
else:
    print(result)
