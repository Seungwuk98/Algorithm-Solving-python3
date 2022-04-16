size = list(map(int, input().split(' ')))
protect_list = [[i for i in range(size[0])], [i for i in range(size[1])]]
for i in range(size[0]):
    protect_row = input()
    for j in range(size[1]):
        if protect_row[j] == 'X':
            if i in protect_list[0]:
                protect_list[0].remove(i)
            if j in protect_list[1]:
                protect_list[1].remove(j)
print(max(len(protect_list[0]), len(protect_list[1])))
