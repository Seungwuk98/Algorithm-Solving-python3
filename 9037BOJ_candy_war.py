for _ in range(int(input())):
    n = int(input())
    candy = [*map(int, input().split())]
    for i in range(n):
        if candy[i] % 2 == 1:
            candy[i] += 1
    count = 0
    while len(set(candy)) != 1:
        candy[-1] = candy[-1]//2
        tmp = candy[-1]
        for i in range(n-1, 0, -1):
            candy[i] += candy[i-1]//2
            candy[i-1] = candy[i-1]//2
            if candy[i] % 2 == 1:
                candy[i] += 1
        candy[0] += tmp
        if candy[0] % 2 == 1:
            candy[0] += 1
        count += 1
    print(count)
