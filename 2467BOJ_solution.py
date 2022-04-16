n = int(input())
a = [*map(int, input().split())]


def twopointer():
    i, j = 0, n-1
    min_value = abs(a[i]+a[j])
    min_idx = (i, j)
    while i < j:
        x = a[i] + a[j]
        abs_x = abs(x)
        if min_value > abs_x:
            min_value = abs_x
            min_idx = i, j
        if x < 0:
            i += 1
        elif x > 0:
            j -= 1
        else:
            break
    return min_idx


min_idx = twopointer()

print(a[min_idx[0]], a[min_idx[1]])
