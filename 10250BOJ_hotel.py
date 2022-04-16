for _ in range(int(input())):
    h, w, n = map(int, input().split())
    a, b = divmod(n, h)
    print(b*100+a+1 if b else h*100+a)
