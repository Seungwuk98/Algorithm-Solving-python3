n = input()
r = 1
m = 1234567891
sum = 0
l = input()
for i in range(len(l)):
    sum += ((ord(l[i])-96)*(r % m)) % m
    r *= 31
print(sum % m)
