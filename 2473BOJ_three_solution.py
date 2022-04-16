n = int(input())
a = [*map(int, input().split())]
a.sort()


def twopointer(k):
    i, j = 0, n-1
    if k == i:
        i += 1
    elif k == j:
        j -= 1
    min_value = abs(a[i]+a[j]+a[k])
    min_idx = (i, j, k)
    while i < j:
        if k == i:
            i += 1
            continue
        elif k == j:
            j -= 1
            continue

        x = a[i] + a[j] + a[k]
        abs_x = abs(x)
        if min_value > abs_x:
            min_value = abs_x
            min_idx = i, j, k
        if x < 0:
            i += 1
        elif x > 0:
            j -= 1
        else:
            break
    return min_value, min_idx


min_value = 1e11
min_idx = ()
for k in range(n):
    min_k, min_k_idx = twopointer(k)
    if min_value > min_k:
        min_value = min_k
        min_idx = min_k_idx


print(*sorted([a[min_idx[0]], a[min_idx[1]], a[min_idx[2]]]))
