import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n, m = map(int, input().split())
g = [[]for _ in range(2*n + 1)]
g_r = [[]for _ in range(2*n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[-a].append(b)
    g[-b].append(a)


def scc(here):
    global sccID, discovered, st, sccCounter, vertexCounter
    ret = discovered[here] = vertexCounter
    vertexCounter += 1

    st.append(here)
    for i in range(len(g[here])):
        there = g[here][i]
        if not discovered[there]:
            ret = min(ret, scc(there))
        elif not sccID[there]:
            ret = min(ret, discovered[there])

    if (ret == discovered[here]):
        while True:
            t = st.pop()
            sccID[t] = sccCounter
            if t == here:
                break
        sccCounter += 1
    return ret


def tarjanSCC():
    global sccID, discovered, st, sccCounter, vertexCounter
    sccID = [0]*(2*n+1)
    discovered = [0]*(2*n+1)
    st = []
    sccCounter, vertexCounter = 1, 1
    for i in range(1, 2*n+1):
        if not discovered[i]:
            scc(i)
    return sccID


def sat():
    label = tarjanSCC()
    for i in range(1, n+1):
        if label[i] == label[-i]:
            return False
    return True


print(+sat())
