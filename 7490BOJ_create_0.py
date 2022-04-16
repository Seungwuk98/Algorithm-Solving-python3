cases = int(input())

result = list()


def plus(count, string):
    string += '+' + str(count)
    return string


def minus(count, string):
    string += '-' + str(count)
    return string


def space(count, string):
    string += ' ' + str(count)
    return string


def makeString(N, count, string):
    if count >= N:
        result.append(string)
        return

    makeString(N, count+1, space(count+1, string))
    makeString(N, count+1, plus(count+1, string))
    makeString(N, count+1, minus(count+1, string))


for _ in range(cases):
    N = int(input())
    makeString(N, 1, '1')
    for i in range(len(result)):
        if eval(result[i].replace(' ', '')) == 0:
            print(result[i])
    result = []
    print()
