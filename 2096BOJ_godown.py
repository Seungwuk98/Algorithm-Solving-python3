import sys
input = sys.stdin.readline

n = int(input())
dp1 = [0]*3
dp2 = [0]*3

for i in range(n):
    mat = [*map(int, input().split())]
    tmp1 = [0]*3
    tmp2 = [0]*3
    tmp1[0] = max(dp1[0], dp1[1]) + mat[0]
    tmp1[1] = max(dp1[0], dp1[1], dp1[2]) + mat[1]
    tmp1[2] = max(dp1[1], dp1[2]) + mat[2]
    tmp2[0] = min(dp2[0], dp2[1]) + mat[0]
    tmp2[1] = min(dp2[0], dp2[1], dp2[2]) + mat[1]
    tmp2[2] = min(dp2[1], dp2[2]) + mat[2]
    dp1 = tmp1
    dp2 = tmp2
print(max(dp1), min(dp2))
