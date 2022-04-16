import sys
input = sys.stdin.readline

n = int(input())
cranes = sorted([*map(int, input().split())], reverse=True)

m = int(input())
boxes = sorted([*map(int, input().split())], reverse=True)

if max(cranes) < max(boxes):
    print(-1)
    sys.exit()
position = [0]*n
checked = [False]*m

result = 0
count = 0
while True:
    if count == len(boxes):
        break
    # for i in range(n):
    #     while position[i] < len(boxes):
    #         if not checked[position[i]] and cranes[i] >= boxes[position[i]]:
    #             checked[position[i]] = True
    #             position[i] += 1
    #             count += 1
    #             break
    #         position[i] += 1
    # result += 1
    for i in range(n):
        for k in range(position[i], m):
            if cranes[i] >= boxes[k] and not checked[k]:
                checked[k] = True
                position[i] = k+1
                count += 1
                break
            position[i] += 1
    result += 1
print(result)
