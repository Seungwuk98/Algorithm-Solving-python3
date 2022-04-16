while True:
    a, b, c = sorted([*map(int, input().split())])
    if a == 0:
        break
    if (c-b)*(c+b) == a**2:
        print('right')
    else:
        print('wrong')
