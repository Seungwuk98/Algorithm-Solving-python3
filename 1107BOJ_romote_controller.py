n = input()
l = len(n)
n = int(n)
m = int(input())
s = set([i for i in range(10)])
if m != 0:
    b = s - set([*map(int, input().split())])
else:
    b = s
b = sorted(list(b))
if not b:
    print(abs(n-100))
    exit(0)
max_b = b[-1]
min_b = b[0]


def make_num(n, b):
    result = []
    for i in b:
        x = n*10+i
        if x <= 1000000:
            result.append(x)
    return result


min_v = abs(n-100)
s = []

x = [0]
for i in range(l-1):
    x = make_num(x[0], [max_b])
if x[0] != 0:
    s += x
x = [0]
for i in range(l):
    y = []
    for j in x:
        y += make_num(j, b)
    x = y
s += x
x = [0]
for i in range(l+1):
    if i == 0 and min_b == 0 and len(b) >= 2:
        x = make_num(x[0], [b[1]])
    else:
        x = make_num(x[0], [min_b])
s += x

for z in s:
    t = abs(n-z)+len(str(z))
    if min_v > t:
        min_v = t
print(min_v)
