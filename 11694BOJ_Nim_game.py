input()
r = 0
for x in map(int, input().split()):
    r ^= x
print('koosaga'if r else'cubelover')
