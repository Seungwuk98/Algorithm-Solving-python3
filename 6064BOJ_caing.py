for _ in range(int(input())):
    m, n, x, y = map(int, input().split())

    year = x
    t = x % n
    if not t:
        t = n
    visit = set([t])
    c = False
    while t != y:
        t = (t+m) % n
        year += m
        if not t:
            t = n
        if t in visit:
            c = True
            print(-1)
            break
        visit.add(t)
    if c:
        continue
    else:
        print(year)
