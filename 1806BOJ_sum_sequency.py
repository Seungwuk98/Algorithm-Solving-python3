n, s = map(int, input().split())
ar = [*map(int, input().split())]
prefix = [0]*(n+1)
for i in range(n):
    prefix[i+1] = prefix[i]+ar[i]
i, j = 0, 1
min_length = n+1
while True:
    sum_window = prefix[j] - prefix[i]
    if j-i < min_length:
        if sum_window >= s:
            min_length = j-i
            i += 1
        elif j == n:
            i += 1
        else:
            j += 1
    else:
        i += 1
    if i == n:
        break
if min_length == n+1:
    print(0)
else:
    print(min_length)
