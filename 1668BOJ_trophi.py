a = int(input())
b = list()
for _ in range(a):
    b.append(int(input()))


def look(b):
    d = 0
    c = 0
    for i in b:
        if d < i:
            c += 1
            d = i
    return c


print(look(b))
b.reverse()
print(look(b))
