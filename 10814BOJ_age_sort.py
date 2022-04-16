cases = int(input())
result = list()
for _ in range(cases):
    result.append(list(input().split(' ')))
result.sort(key=lambda x: int(x[0]))
for i, v in result:
    print(i, v)
