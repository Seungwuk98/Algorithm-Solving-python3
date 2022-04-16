rules = list(map(int, input().split(' ')))
cards = list(map(int, input().split(' ')))
max = 0

for i in range(rules[0]):
    for j in range(i+1, rules[0]):
        for k in range(j+1, rules[0]):
            sum = cards[i] + cards[j] + cards[k]
            if max < sum and sum <= rules[1]:
                max = sum

print(max)
