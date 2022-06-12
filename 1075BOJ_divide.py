from re import I


n = int(input())//100*100
f = int(input())
for i in range(100):
    if (n+i) % f == 0:
        print("{:02d}".format(i))
        break
