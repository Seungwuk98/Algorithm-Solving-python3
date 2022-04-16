a, b, v = map(int, input().split())
d, r = divmod(v-a, a-b)
if r != 0:
    d += 1
print(d+1)
