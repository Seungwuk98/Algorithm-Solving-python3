
def chk(n, mine, num, cnt):
    mx = max(num)
    c = False
    result = 0
    for i in range(n):
        if num[i] == mx:
            c = True
            mine[i] = '*'
            tmp = num[i]
            num[i] = 0
            result = max(chk(n, mine, num, cnt+1), result)
            mine[i] = '#'
            num[i] = tmp
    if c:
        return cnt
    else:
        return result


for _ in range(int(input())):
    n = int(input())
    num = [*map(int, input().split())]
    mine = [*input()]
    print(chk(n, mine, num, 0))
