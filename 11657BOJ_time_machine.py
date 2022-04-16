n, m = map(int, input().split())
edge = [[*map(int, input().split())]for _ in range(m)]


def belmanford(n, edge, s):
    distance = [1e9]*(n+1)
    distance[s] = 0
    for i in range(n):
        for node, next_node, next_dist in edge:
            if distance[node] != 1e9:
                from_start = distance[node]+next_dist
                if from_start < distance[next_node]:
                    distance[next_node] = from_start
                    if i == n-1:
                        return -1
    for i in range(n+1):
        if distance[i] == 1e9:
            distance[i] = -1
    return distance


distance = belmanford(n, edge, 1)
if distance == -1:
    print(-1)
else:
    print('\n'.join(map(str, distance[2:])))
