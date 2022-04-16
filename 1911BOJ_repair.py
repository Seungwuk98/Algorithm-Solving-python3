import sys
input = sys.stdin.readline

n, l = map(int, input().split())

mat = [[*map(int, input().split())]for _ in range(n)]
mat.sort()

now = 0
cnt = 0
for s, e in mat:
    if now < s:
        now = s
    diff = e - now
    d, r = divmod(diff, l)
    if r:
        cnt += d+1
        now += l*(d+1)
    else:
        cnt += d
        now += l*d
print(cnt)
