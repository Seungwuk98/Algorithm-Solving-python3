import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    point = [0]+[*map(int, input().split())]
    r = set()
    visit = [False]*(n+1)
    for i in range(1, n+1):
        s = [i]
        now_visit = set([i])
        now = i
        visit[now] = True
        while True:
            next = point[now]
            if next in now_visit:
                r.add(next)
                while s[-1] != next:
                    r.add(s.pop())
                break
            if visit[next]:
                break
            visit[next] = True
            now_visit.add(next)
            s.append(next)
            now = next
    print(n-len(r))
