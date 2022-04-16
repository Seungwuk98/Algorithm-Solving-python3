n = int(input())
mat = [[*map(int, input().split())]for _ in range(n)]
result = 0


def ck(i, j):
    l = i + (n-j-1)
    for k in range(l+1):
        if k < n and 0 <= k+n-1-l < n and cmat[k][k+n-1-l]:
            return False
    return True


def dfs(l, level):
    global result
    if l >= 2*n-1:
        result = max(result, level)
        return
    c = True
    for i in range(l+1):
        if i < n and l-i < n and mat[i][l-i] and ck(i, l-i):
            c = False
            cmat[i][l-i] = 1
            dfs(l+1, level+1)
            cmat[i][l-i] = 0
    if c:
        dfs(l+1, level)


cmat = [[0]*n for _ in range(n)]
dfs(0, 0)
print(result)
