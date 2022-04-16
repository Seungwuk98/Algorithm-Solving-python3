import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
c = dict()
for x in map(int, input().split()):
    if x not in c:
        c[x] = 0
    c[x] += 1
m = int(input())
for y in map(int, input().split()):
    if y not in c:
        print('0 ')
    else:
        print(str(c[y])+' ')
