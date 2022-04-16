s = [*map('0b{}'.format, input().split())]

print(bin(int(s[0], 2)+int(s[1], 2))[2:])
