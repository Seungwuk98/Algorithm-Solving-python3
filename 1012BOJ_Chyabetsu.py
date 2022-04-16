import sys
input = sys.stdin.readline
sys.setrecursionlimit(99999)


def dfs(i, j, m, n):
    if [i, j] in visited:
        return
    visited.append([i, j])
    for v, w in [[i+1, j], [i, j+1], [i-1, j], [i, j-1]]:
        if [v, w] not in visited and v < m and v >= 0 and w < n and w >= 0:
            if c[v][w] == 1:
                dfs(v, w, m, n)


a = int(input())
for _ in range(a):
    m, n, k = map(int, input().split())
    b = [[*map(int, input().split())] for _ in range(k)]
    c = [[0]*n for _ in range(m)]
    for i, j in b:
        c[i][j] = 1

    count = 0
    visited = []
    for i, j in b:
        if [i, j] in visited:
            continue
        dfs(i, j, m, n)
        count += 1
    print(count)
