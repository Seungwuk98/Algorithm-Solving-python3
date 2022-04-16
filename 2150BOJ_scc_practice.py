import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

v, e = map(int, input().split())
g = [[]for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    g[a].append(b)

result = []


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
        x = []
        while True:
            t = st.pop()
            sccID[t] = sccCounter
            x.append(t)
            if t == here:
                break
        x.sort()
        x.append(-1)
        result.append(x)
        sccCounter += 1
    return ret


def tarjanSCC():
    global sccID, discovered, st, sccCounter, vertexCounter
    sccID = [0]*(v+1)
    discovered = [0]*(v+1)
    st = []
    sccCounter, vertexCounter = 1, 1
    for i in range(1, v+1):
        if not discovered[i]:
            scc(i)
    return sccID


tarjanSCC()
result.sort()
print(len(result))
for x in result:
    print(*x)
