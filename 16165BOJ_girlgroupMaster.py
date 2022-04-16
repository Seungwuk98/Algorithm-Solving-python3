n, m = map(int, input().split())
G = dict()
s = dict()
for _ in range(n):
    g = input()
    G[g] = []
    r = int(input())
    for _ in range(r):
        w = input()
        G[g].append(w)
        s[w] = g

for _ in range(m):
    q = input()
    t = int(input())
    if t == 1:
        print(s[q])
    else:
        for i in sorted(G[q]):
            print(i)
