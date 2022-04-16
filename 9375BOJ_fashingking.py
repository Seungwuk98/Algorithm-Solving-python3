import sys
from itertools import combinations
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    d = {}
    for _ in range(n):
        c, s = input().strip('\n').split()
        if s not in d:
            d[s] = 0
        d[s] += 1

    l = len(d)
    counts = list(d.values())
    t = 1
    for x in counts:
        t *= x+1
    print(t-1)
