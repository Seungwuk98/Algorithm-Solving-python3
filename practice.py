import sys
input = sys.stdin.readline

n = int(input())
arr = [0]+[int(input())for _ in range(n)]


def percolate_down(arr, n, s=1):
    while ((s << 1) <= n):
        nxt = (s << 1) if arr[s << 1] > arr[s] else s
        nxt = (s << 1 | 1) if (s << 1 | 1) <= n and arr[s <<
                                                        1 | 1] > arr[nxt] else nxt
        if s == nxt:
            return
        arr[nxt], arr[s] = arr[s], arr[nxt]
        s = nxt


for i in range(n >> 1, 0, -1):
    percolate_down(arr, n, i)
for i in range(n, 1, -1):
    arr[1], arr[i] = arr[i], arr[1]
    percolate_down(arr, i-1)

for i in range(1, n+1):
    sys.stdout.write(str(arr[i])+'\n')
