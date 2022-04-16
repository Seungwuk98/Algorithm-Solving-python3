def f(n):
    p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if n <= 10:
        return p[n]
    for i in range(11, n+1):
        p.append(p[i-1]+p[i-5])
    return p[n]


for _ in range(int(input())):
    print(f(int(input())))
