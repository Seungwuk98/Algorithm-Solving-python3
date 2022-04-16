cases = int(input())
result = []

for i in range(cases):
    count = 1
    documents, interested = map(int, input().split(' '))
    priority = list(map(int, input().split(' ')))
    pq = [(priority[i], i) for i in range(documents)]
    while pq:
        max_priority = max([x[0] for x in pq])
        while pq[0][0] != max_priority:
            pq.append(pq.pop(0))
        data = pq.pop(0)
        if data[1] == interested:
            result.append(count)
            break
        count += 1

for _ in range(cases):
    print(result[_])
