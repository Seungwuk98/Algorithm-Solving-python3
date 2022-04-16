l, c = map(int, input().split())
alphabet = sorted([*input().split()])
mList = set(['a', 'e', 'i', 'o', 'u'])
hava_m = sorted(list(mList & set(alphabet)))
visit = list()


def available(x):
    length = len(x)
    m = 0
    for i in range(length):
        if x[i] in mList:
            m += 1
    if length < l:
        if length == 0:
            return True
        if m == 0 and x[-1] > hava_m[-1]:
            return False
        else:
            return True
    elif m < 1 or length - m < 2:
        return False
    else:
        return True


def dfs(x, start):
    length = len(x)
    if not available(x):
        return
    elif length == l:
        visit.append(x)
        return
    for i in range(start, c+1-(l-length)):
        dfs(x+alphabet[i], i+1)


dfs('', 0)
for i in visit:
    print(i)
