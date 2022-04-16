n, B, C = map(int, input().split())
arr = [*map(int, input().split())]
if B <= C:
    print(B*sum(arr))
else:
    a, b, c = 0, 0, 0
    cnt = 0
    for i in range(n):
        tmp = min(arr[i], a)
        cnt += C*tmp
        c = min(arr[i]-tmp, b)
        cnt += C*c
        a = arr[i]-tmp-c
        cnt += B*a
        b = tmp
    print(cnt)
