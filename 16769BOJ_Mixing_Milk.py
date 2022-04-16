c = []
m = []
for i, j in [map(int, input().split())for i in range(3)]:
    c.append(i)
    m.append(j)


def pour(i, j):
    if c[j]-m[j] < m[i]:
        m[i] = m[i] - c[j] + m[j]
        m[j] = c[j]
    else:
        m[j] = m[i]+m[j]
        m[i] = 0


for _ in range(100):
    pour(_ % 3, (_+1) % 3)

for i in m:
    print(i)
