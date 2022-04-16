from itertools import permutations

n = int(input())
arr = [*map(int, input().split())]
d = '+-*/'
op = []
c = 0
for x in map(int, input().split()):
    while x:
        op.append(d[c])
        x -= 1
    c += 1
op_comb = permutations(op)


def calculate(arr, comb):
    prev = arr[0]
    for i in range(1, n):
        now = arr[i]
        oper = comb[i-1]
        if oper == '+':
            x = prev + now
        elif oper == '-':
            x = prev - now
        elif oper == '*':
            x = prev * now
        else:
            x = -((-prev) // now) if prev < 0 else prev//now
        prev = x
    return prev


_max = -int(1e10)
_min = int(1e10)
for comb in op_comb:
    x = calculate(arr, comb)
    _max = max(_max, x)
    _min = min(_min, x)
print(_max, _min)
