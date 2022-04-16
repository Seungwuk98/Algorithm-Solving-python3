for _ in range(int(input())):
    s1 = []
    for i in input():
        if i == '(':
            s1.append(i)
        elif i == ')':
            try:
                s1.pop()
            except:
                print('NO')
                break
    else:
        if not s1:
            print('YES')
        else:
            print('NO')
