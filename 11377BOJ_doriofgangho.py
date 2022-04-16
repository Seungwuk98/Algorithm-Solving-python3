import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
g = [[]for _ in range(2*n+1)]
for i in range(1, n+1):
    work = [*map(int, input().split())]
    for j in range(1, work[0]+1):
        g[i].append(work[j])
        g[n+i].append(work[j])

amatch = [0]*(2*n+1)
bmatch = [0]*(m+1)


def dfs(a):
    global double
    if visit[a] or (amatch[a+n if a+n <= 2*n else a-n] and double == k):
        return False
    visit[a] = True
    for b in g[a]:
        if not bmatch[b] or dfs(bmatch[b]):
            if not amatch[a] and amatch[a+n if a+n <= 2*n else a-n]:
                double += 1
            amatch[a] = b
            bmatch[b] = a
            return True
    return False


size = 0
double = 0
for i in range(1, 2*n+1):
    visit = [False]*(2*n+1)
    if dfs(i):
        size += 1
print(size)
