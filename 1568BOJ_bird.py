birds = int(input())
second = [0]


def birdscount(birds):
    if birds == 0:
        return
    n = int(birds**0.5)
    while (n+1)*(n+2)/2 <= birds:
        n += 1
    second[0] += n
    birdscount(birds - n*(n+1)//2)


birdscount(birds)
print(second[0])
