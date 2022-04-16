from collections import deque

a, b, s = map(int, input().split())
g = [[]for _ in range(a+1)]
for _ in range(b):
    k, v = map(int, input().split())
    g[k].append(v)
    g[v].append(k)


def b(g, s):
    v = []
    q = deque([s])

    while q:
        n = q.popleft()
        if n in v:
            continue
        v.append(n)
        d = sorted(g[n])
        q.extend(d)
    return v


def d(g, s):
    v = []
    q = [s]

    while q:
        n = q.pop()
        if n in v:
            continue
        v.append(n)
        d = sorted(g[n], reverse=True)
        q.extend(d)
    return v


print(*d(g, s))
print(*b(g, s))
