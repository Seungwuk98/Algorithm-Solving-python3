N = int(input())
A = set(map(int, input().split(' ')))
M = int(input())
B = list(map(int, input().split(' ')))
C = set(B)

X = A & C
for x in B:
    if x in X:
        print(1)
    else:
        print(0)
