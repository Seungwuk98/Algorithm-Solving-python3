def up_left(j):
    return 1 if arr[0][j-1]+arr[0][j] <= w else 2


def down_left(j):
    return 1 if arr[1][j-1]+arr[1][j] <= w else 2


def st(j):
    return 1 if arr[0][j]+arr[1][j] <= w else 2


def go_dp(x):
    for i in range(2, n-1):
        b[i] = min(a[i-1]+1, c[i-1]+up_left(i))
        c[i] = min(a[i-1]+1, b[i-1]+down_left(i))
        a[i] = min(a[i-1]+st(i), c[i]+1)
    if not x:
        b[-1] = min(a[-1-1]+1, c[-1-1]+up_left(-1))
        c[-1] = min(a[-1-1]+1, b[-1-1]+down_left(-1))
        a[-1] = min(a[-1-1]+st(-1), c[-1]+1)
    elif x == 1:
        b[-1] = a[-2]
        a[-1] = min(b[-1]+1, b[-2]+down_left(-1))
    elif x == 2:
        c[-1] = a[-2]
        a[-1] = min(c[-1]+1, c[-2]+up_left(-1))
    else:
        a[-1] = a[-2]
    return a[-1]


INF = int(1e9)
for _ in range(int(input())):
    n, w = map(int, input().split())
    arr = [[*map(int, input().split())]for _ in range(2)]
    if n == 1:
        print(st(0))
        continue
    elif n == 2:
        print(min(st(0)+st(1), up_left(1)+down_left(1)))
        continue

    a = [INF]*n
    b = [INF]*n
    c = [INF]*n
    a[0] = st(0)
    b[0] = 1
    c[0] = 1
    a[1] = min(a[0]+st(1), up_left(1)+down_left(1))
    b[1] = min(a[0]+1, up_left(1)+1)
    c[1] = min(a[0]+1, down_left(1)+1)
    result = go_dp(0)
    if arr[0][0] + arr[0][-1] <= w:
        a = [INF]*n
        b = [INF]*n
        c = [INF]*n
        a[0] = 2
        b[0] = 1
        b[1] = 3
        c[1] = 1+down_left(1)
        a[1] = min(a[0]+st(1), b[1]+1, c[1]+1)
        result = min(result, go_dp(1))
    if arr[1][0] + arr[1][-1] <= w:
        a = [INF]*n
        b = [INF]*n
        c = [INF]*n
        a[0] = 2
        c[0] = 1
        c[1] = 3
        b[1] = 1+up_left(1)
        a[1] = min(a[0]+st(1), b[1]+1, c[1]+1)
        result = min(result, go_dp(2))
    if arr[1][0]+arr[1][-1] <= w and arr[0][0]+arr[0][-1] <= w:
        a = [INF]*n
        b = [INF]*n
        c = [INF]*n
        a[0] = 2
        b[1] = 3
        c[1] = 3
        a[1] = a[0]+st(1)
        result = min(result, go_dp(3))
    print(result)
