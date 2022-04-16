n = input()
a = set(map(int, input().split()))
m = input()
for i in map(int, input().split()):
    print(+(i in a))
