from collections import deque
for _ in range(int(input())):
    f = input()
    n = int(input())
    arr = input()
    arr = deque([*arr[1:-1].split(',')])
    r = 0
    for i in f:
        if i == 'R':
            r = (r+1)%2
        elif i == 'D':
            if n == 0:
                print('error')
                break
            try:
                if r == 0:
                    arr.popleft()
                else:
                    arr.pop()
            except:
                print('error')
                break
    else:
        if r==0:
            print('['+','.join(list(arr)) + ']')
        elif r==1:
            arr.reverse()
            print('['+','.join(list(arr)) + ']')
