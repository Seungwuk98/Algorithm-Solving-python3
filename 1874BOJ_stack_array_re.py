re = int(input())
stack = list()
push_pop_list = list()
i = 1

for j in range(re):
    num = int(input())
    while i <= num:
        stack.append(i)
        push_pop_list.append('+')
        i += 1
    if stack[-1] == num:
        stack.pop()
        push_pop_list.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(push_pop_list))
