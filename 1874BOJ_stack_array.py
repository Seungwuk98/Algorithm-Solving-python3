num = int(input())
array = list()
last_pushed = 0
push_pop_list = list()
left_list = list()
available = True

for i in range(num):
    array.append(int(input()))
    if array[i] > last_pushed:
        for j in range(array[i] - last_pushed):
            push_pop_list.append('+')
            left_list.append(last_pushed+1)
            last_pushed += 1
    if left_list.pop() != array[i]:
        available = False
    push_pop_list.append('-')


if available:
    for i in range(len(push_pop_list)):
        print(push_pop_list[i])
else:
    print('NO')
