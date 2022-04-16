import sys
input = sys.stdin.readline
a = int(input())
b = [0] * (500000+1)
for _ in range(a):
    b[int(input())] += 1

left_num = []
no_num = []
for i in range(1, 500000+1):
    if b[i] != 0:
        for _ in range(b[i]-1):
            left_num.append(i)
        if i > a:
            left_num.append(i)
    elif i <= a:
        no_num.append(i)
if len(no_num) > len(left_num):
    for _ in range(len(no_num)-len(left_num)):
        no_num.pop(0)
result = 0
for i in range(len(left_num)):
    result += abs(left_num[i]-no_num[i])
print(result)
