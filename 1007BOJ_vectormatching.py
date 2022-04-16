from itertools import combinations
for _ in range(int(input())):
    n = int(input())
    points = [[*map(int, input().split())]for _ in range(n)]
    e_set = set(range(n))
    a_comb = combinations(range(n), n//2)
    r = 1e9
    for a_set in a_comb:
        b_set = e_set - set(a_set)
        a, b = 0, 0
        for idx in a_set:
            a += points[idx][0]
            b += points[idx][1]
        for idx in b_set:
            a -= points[idx][0]
            b -= points[idx][1]
        r = min(r, (a*a+b*b)**0.5)
    print(r)
