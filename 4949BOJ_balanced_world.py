n = input()
while n != '.':
    s1 = []
    for i in n:
        if i == '(':
            s1.append('(')
        elif i == ')':
            try:
                a = s1.pop()
                if a != '(':
                    print('no')
                    break
            except:
                print('no')
                break
        elif i == '[':
            s1.append('[')
        elif i == ']':
            try:
                b = s1.pop()
                if b != '[':
                    print('no')
                    break
            except:
                print('no')
                break
        else:
            continue
    else:
        if not s1:
            print('yes')
        else:
            print('no')
    n = input()
