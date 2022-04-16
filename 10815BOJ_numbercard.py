n = int(input())
a = {*map(int, input().split())}
m = int(input())
r = []
for x in map(int, input().split()):
    r.append(+(x in a))
print(*r)
