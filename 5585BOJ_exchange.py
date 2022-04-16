a = 1000-int(input())
s = 0
for i in [500, 100, 50, 10, 5, 1]:
    b = a//i
    a -= b*i
    s += b
print(s)
