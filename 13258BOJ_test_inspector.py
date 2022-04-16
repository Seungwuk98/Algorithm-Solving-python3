n = int(input())
a = [*map(int, input().split())]
b, c = map(int, input().split())
r = 0
for x in a:
    r += 1
    t, d = divmod(max(x-b, 0), c)
    if d:
        r += t+1
    else:
        r += t
print(r)
