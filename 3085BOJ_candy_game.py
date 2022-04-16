n = int(input())
arr = [[*input()]for _ in range(n)]
d = ((1, 0), (-1, 0), (0, 1), (0, -1))


def check(n, arr):
    ret = 1
    for i in range(n):
        ret1 = ret2 = 1
        for j in range(1, n):
            if arr[i][j-1] == arr[i][j]:
                ret1 += 1
                ret = max(ret, ret1)
            else:
                ret1 = 1
            if arr[j-1][i] == arr[j][i]:
                ret2 += 1
                ret = max(ret, ret2)
            else:
                ret2 = 1
    return ret


result = 1
for i in range(n):
    for j in range(n):
        for di, dj in d:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n:
                arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
                result = max(result, check(n, arr))
                arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]

print(result)
