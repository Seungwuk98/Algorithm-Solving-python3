n, k = map(int, input().split())
c = sorted([int(input())for _ in range(n)], reverse=True)
r = 0
i = 0
while k:
    x, k = divmod(k, c[i])
    r += x
    i += 1
print(r)
