n = int(input())
p = [*map(int, input().split())]

c = [[]for _ in range(n)]
for i in range(n):
    if p[i] == -1:
        root = i
    else:
        j = p[i]
        c[j].append(i)
d = int(input())
if p[d] == -1:
    print(0)
    exit(0)
c[p[d]].remove(d)

result = 0


def dfs(node):
    global result
    if not c[node]:
        result += 1
        return
    for next in c[node]:
        dfs(next)


dfs(root)
print(result)
