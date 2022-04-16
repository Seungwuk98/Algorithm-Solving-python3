n, m = map(int, input().split())
chess = [[*input()]for _ in range(n)]
w = 'W', 'B'
b = 'B', 'W'


def compare(i, j):
    r1 = 0
    r2 = 0
    for di in range(8):
        for dj in range(8):
            ni = i+di
            nj = j+dj
            if chess[ni][nj] != w[(di+dj) % 2]:
                r1 += 1
            if chess[ni][nj] != b[(di+dj) % 2]:
                r2 += 1
    return min(r1, r2)


min_value = 25000
for i in range(n-7):
    for j in range(m-7):
        min_value = min(min_value, compare(i, j))
print(min_value)
