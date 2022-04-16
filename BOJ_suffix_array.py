from random import randint
import sys
s = sys.stdin.readline().rstrip()
t = 1
n = len(s)


def compare(a, b):
    if group[a] != group[b]:
        return group[a] > group[b]
    else:
        return group[a+t] > group[b+t]


def qsort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop(randint(0, len(arr)-1))
    left = [x for x in arr if compare(pivot, x)]
    right = [x for x in arr if not compare(pivot, x)]
    return qsort(left) + [pivot] + qsort(right)


group = [ord(s[x]) for x in range(n)]+[-1]
suffix = [*range(n)]

while t < n:
    suffix = qsort(suffix)
    if t*2 >= n:
        break
    newgroup = [-1]*(n+1)
    newgroup[0] = 0
    for i in range(n-1):
        if compare(suffix[i], suffix[i+1]):
            newgroup[suffix[i+1]] = newgroup[suffix[i]]
        else:
            newgroup[suffix[i+1]] = newgroup[suffix[i]]+1
    group = newgroup
    t <<= 1
print(*map(lambda x: x+1, suffix))

lcp = [0]*n
isuffix = [0]*n
for i in range(n):
    isuffix[suffix[i]] = i

for i in range(n):
    j = isuffix[i]  # i번 째 접미사가 사전 순으로 몇번째?
    l = lcp[j]  # j의 lcp는 최소 몇개?
    if not j:
        lcp[j] = 'x'
        continue
    k = suffix[j-1]  # 사전순 j-1의 접미사는 몇 번째 ?
    while k+l < n and i+l < n and s[i+l] == s[k+l]:  # 될 때까지 l 증가
        l += 1
    lcp[j] = l  # j의 lcp는 l개
    # i+1부터는 최소 l-1개
    x = i+1
    l -= 1
    while l > 0 and x < n:
        j = isuffix[x]
        lcp[j] = l
        x += 1
        l -= 1


print(*lcp)
