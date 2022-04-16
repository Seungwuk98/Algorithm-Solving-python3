import copy
n, m = map(int, input().split())
things = [list(map(int, input().split()))for _ in range(n)]
comb = {0: 0}
visitList = []


def backpack(weight, value, idx):
    weight += things[idx][0]
    value += things[idx][1]
    if weight > m:
        return

    if weight not in comb:
        comb[weight] = value
    elif value < comb[weight]:
        return
    else:
        comb[weight] = value
    for i in range(idx+1, n):
        backpack(weight, value, i)


for i in range(n):
    backpack(0, 0, i)

# print(comb)
print(max(comb.values()))
