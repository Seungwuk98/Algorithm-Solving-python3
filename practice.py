n = input()[::-1]
s = ''
for x in n:
    y = int(x)
    for _ in range(3):
        s += str(y & 1)
        y >>= 1
s = s.rstrip('0')
if s:
    print(s[::-1])
else:
    print(0)
