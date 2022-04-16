import sys
mat = sys.stdin.readlines()
for i in range(len(mat)):
    mat[i] = '0b'+mat[i].strip('\n').replace('O', '1')
    mat[i] = int(mat[i].replace('#', '0'), 2)


def switch(mat, i, j):
    if i > 0:
        mat[i-1] ^= 1 << j
    tmp = 1 << j
    if i < 9:
        mat[i+1] ^= 1 << j
    if j > 0:
        tmp |= 1 << (j-1)
    if j < 9:
        tmp |= 1 << (j+1)
    mat[i] ^= tmp


def greed(mat):
    global result
    r = 0
    for i in range(1, 10):
        for j in range(10):
            if mat[i-1] & (1 << j):
                r += 1
                if r > result:
                    return 10000
                switch(mat, i, j)
    if mat[-1] == 0:
        return r
    else:
        return 10000


result = 10000
result = min(greed(mat[::1]), result)
qry = (1 << 10)-1
subset = qry
while subset:
    i, j = 0, 0
    tmp = subset
    tmat = mat[::1]
    while tmp:
        if tmp & 1:
            switch(tmat, 0, i)
            j += 1
        tmp >>= 1
        i += 1
    result = min(result, greed(tmat)+j)
    subset = (subset-1) & qry
if result != 10000:
    print(result)
else:
    print(-1)
