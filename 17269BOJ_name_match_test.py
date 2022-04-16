n, m = map(int, input().split())
a, b = input().split()
a = [*a]
b = [*b]
h = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3,
     2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
min_len = min(len(a), len(b))
max_len = max(len(a), len(b))
r = [0 for i in range(len(a)+len(b))]
for i in range(min_len):
    r[i*2] = h[ord(a[i])-65]
    r[i*2+1] = h[ord(b[i])-65]
for j in range(max_len-min_len):
    if len(a) > len(b):
        r[min_len*2+j] = h[ord(a[j+min_len])-65]
    elif len(a) < len(b):
        r[min_len*2+j] = h[ord(b[j+min_len])-65]

i = len(r)
while i != 2:
    for j in range(i-1):
        r[j] = (r[j]+r[j+1]) % 10
    i -= 1
print(str(r[0]*10 + r[1])+'%')
