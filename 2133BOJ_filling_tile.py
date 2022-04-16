t = int(input())//2
k = 3
l = 11
for i in range(3, t+1):
    x = (4*l-k) % 1000000007
    k = l
    l = x
if t == 2:
    print(l)
elif t == 1:
    print(k)
else:
    print(x)

c1 = 3**0.5-3
a1 = 2-3**0.5
c2 = 3**0.5+3
a2 = 2+3**0.5
print(int((-c1*(a1**t)+c2*(a2**t))/6+0.5) % 1000000007)


def method1(t):
    k = 3
    l = 11
    for i in range(3, t+1):
        x = (4*l-k) % 1000000007
        k = l
        l = x
    if t == 2:
        return l
    elif t == 1:
        return k
    else:
        return x


def method2(t):
    c1 = 3**0.5-3
    a1 = 2-3**0.5
    c2 = 3**0.5+3
    a2 = 2+3**0.5
    return int((-c1*(a1**t)+c2*(a2**t))/6+0.5) % 1000000007


for i in range(3, 1000):
    if method1(i) == method2(i):
        print('o')
    else:
        print(i, method1(i), method2(i))
        print('------------x----------')
