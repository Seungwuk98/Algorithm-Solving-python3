cases = int(input())
result = []

for _ in range(cases):
    stack1 = list()
    stack2 = list()
    check = input()

    for i in check:
        if i == '<':
            if stack1:
                stack2.append(stack1.pop())
        elif i == '>':
            if stack2:
                stack1.append(stack2.pop())
        elif i == '-':
            if stack1:
                stack1.pop()
        else:
            stack1.append(i)
    stack1.extend(reversed(stack2))
    for x in range(len(stack1)):
        print(stack1[x], end='')
    print()
