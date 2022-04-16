from heapq import *
n = int(input())
p = [[*map(float, input().split())]for _ in range(n)]


def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(0.5)


g = [[]for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            p1, p2 = p[i], p[j]
            dist = distance(p1, p2)
            g[i].append((dist, j))
            g[j].append((dist, i))

edge = g[0]
heapify(edge)
result = 0
visit = [False]*100
visit[0] = True
while edge:
    dist, now = heappop(edge)
    if visit[now]:
        continue
    visit[now] = True
    result += dist
    for next_dist, next_node in g[now]:
        if not visit[next_node]:
            heappush(edge, (next_dist, next_node))
print(result)
