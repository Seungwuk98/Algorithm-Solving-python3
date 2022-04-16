import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

v, e = map(int, input().split())
g = [[]for _ in range(v+1)]
g_r = [[]for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    g[a].append(b)
    g_r[b].append(a)

num_arr = [0]*(v+1)
num = 0


def dfs(node):
    global num

    for next in g[node]:
        if not visit[next]:
            visit[next] = True
            dfs(next)
    num_arr[node] = num
    num += 1


def dfs2(node):
    for next in g_r[node]:
        if not visit[next]:
            scc_com.append(next)
            visit[next] = True
            dfs2(next)


visit = [False]*(v+1)
for i in range(1, v+1):
    if not visit[i]:
        visit[i] = True
        dfs(i)

num_rev = []
for idx, x in enumerate(num_arr):
    num_rev.append((x, idx))
num_rev.sort(reverse=True)
visit = [False]*(v+1)
scc = []
for x, idx in num_rev:
    if not visit[idx] and idx:
        visit[idx] = True
        scc_com = [idx]
        dfs2(idx)
        scc_com.sort()
        scc_com.append(-1)
        scc.append(scc_com)
scc.sort()
print(len(scc))
for x in scc:
    print(*x)
