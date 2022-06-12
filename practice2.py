s1 = [input() for _ in range(1000)]
s2 = [input() for _ in range(1000)]

print([s1[i] != s2[i] for i in range(1000) if s1[i] != s2[i]])
