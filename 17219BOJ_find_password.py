import sys
n, m = map(int, input().split())
input = sys.stdin.readline
d = {}

for _ in range(n):
    s, p = input().strip('\n').split()
    d[s] = p

for _ in range(m):
    print(d[input().strip('\n')])
