from typing import OrderedDict


a = int(input())
selled = dict()
for _ in range(a):
    book = input()
    if book not in selled.keys():
        selled[book] = 1
    else:
        selled[book] += 1

max = max(selled.values())
max_list = list()
for k, v in selled.items():
    if v == max:
        max_list.append(k)
max_list.sort()
print(max_list[0])
