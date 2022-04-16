import sys
input = sys.stdin.readline
print = sys.stdout.write
s = [*input().rstrip()]
s2 = []

for _ in range(int(input())):
    o = input().rstrip().split()
    if o[0] == 'P':
        s.append(o[1])
    elif o[0] == 'L':
        if s:
            s2.append(s.pop())
    elif o[0] == 'D':
        if s2:
            s.append(s2.pop())
    else:
        if s:
            s.pop()
s2.reverse()
s = s+s2
print(''.join(s))
