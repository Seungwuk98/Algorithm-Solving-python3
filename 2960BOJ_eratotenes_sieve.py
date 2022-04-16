n, k = map(int, input().split())
count = 0
isprime = [True]*(n+1)
for i in range(2, n+1):
    if isprime[i]:
        for j in range(i, n+1, i):
            if isprime[j]:
                count += 1
                isprime[j] = False
                if count == k:
                    print(j)
                    exit(0)
