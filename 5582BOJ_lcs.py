x, y = input, range
a = x()
b = x()
n = len(a)
m = len(b)
p = [0]*(m+1)

r = 0
for i in y(1, n+1):
    w = [0]*(m+1)
    for j in y(1, m+1):
        if a[i-1] == b[j-1]:
            w[j] = p[j-1] + 1
            r = max(r, w[j])
    p = w

print(r)
