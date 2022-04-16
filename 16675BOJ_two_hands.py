mL, mR, tL, tR = input().split()


def compare(x, y):
    if (x == 'R' and y == 'S') or (x == 'S' and y == 'P') or (x == 'P' and y == 'R'):
        return True
    else:
        return False


for i in [mL, mR]:
    check = True
    for j in [tL, tR]:
        if not compare(i, j):
            check = False
    if check:
        print('MS')
        exit(0)

for i in [tL, tR]:
    check = True
    for j in [mL, mR]:
        if not compare(i, j):
            check = False
    if check:
        print('TK')
        exit(0)

print('?')
