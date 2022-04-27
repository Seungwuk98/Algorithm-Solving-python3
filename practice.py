
def switching_mergesort(arr):
    b = arr[:]
    msort(0, len(arr)-1, arr, b)


def msort(p, r, a, b):
    if (p < r):
        q = p+r >> 1
        msort(p, q, b, a)
        msort(q+1, r, b, a)
        switching_merge(p, q, r, b, a)


def switching_merge(p, q, r, c, d):
    i, j, t = p, q+1, p
    while i <= q and j <= r:
        if c[i] <= c[j]:
            d[t] = c[i]
            i += 1
        else:
            d[t] = c[j]
            j += 1
        t += 1
    while i <= q:
        d[t] = c[i]
        t += 1
        i += 1
    while j <= r:
        d[t] = c[j]
        t += 1
        j += 1


n = int(input())
arr = [int(input())for _ in range(n)]
switching_mergesort(arr)
print(' '.join(map(str, arr)))
