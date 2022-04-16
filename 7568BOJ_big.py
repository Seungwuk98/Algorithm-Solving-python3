def big(a, b):
    x1, y1 = a
    x2, y2 = b
    if x1 < x2 and y1 < y2:
        return True
    else:
        return False


n = int(input())
h = [[*map(int, input().split())]for _ in range(n)]

x = [1]*n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if big(h[i], h[j]):
            x[i] += 1

print(*x)
