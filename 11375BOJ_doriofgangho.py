import sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[]for _ in range(n+1)]
for i in range(1, n+1):
    work = [*map(int, input().split())]
    for j in range(1, work[0]+1):
        g[i].append(work[j])

amatch = [0]*(n+1)
bmatch = [0]*(m+1)


def dfs(a):
    if visit[a]:
        return False
    visit[a] = True
    for b in g[a]:
        if not bmatch[b] or dfs(bmatch[b]):
            amatch[a] = b
            bmatch[b] = a
            return True
    return False


size = 0
for i in range(1, n+1):
    visit = [False]*(n+1)
    if dfs(i):
        size += 1
print(size)
