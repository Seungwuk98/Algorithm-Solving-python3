from collections import defaultdict
d = defaultdict(int)
for _ in range(int(input())):
    d[input()[0]] += 1
a = ''.join(sorted([x for x in d if d[x] >= 5]))
if a:
    print(a)
else:
    print('PREDAJA')
