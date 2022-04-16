import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [[0]*(n+1)]+[[0]+[*map(int, input().split())]for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, n+1):
        mat[i][j] = mat[i][j] + mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]

r = []
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    sum = mat[x2][y2] - mat[x2][y1-1] - mat[x1-1][y2] + mat[x1-1][y1-1]
    r.append(sum)

print('\n'.join(map(str, r)))
