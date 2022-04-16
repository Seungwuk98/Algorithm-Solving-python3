A, B, C = map(int, input().split())


def fpow(A, B, C):
    if B == 1:
        return A % C
    if B & 1:
        return (fpow(A, B >> 1, C)**2*A) % C
    else:
        return (fpow(A, B >> 1, C)**2) % C


# def fpow(A, B, C):
#     if B == 1:
#         return A % C
#     result = 1
#     while B:
#         if B & 1:
#             result = (result*A) % C
#         A = (A*A) % C
#         B >>= 1
#     return result


print(fpow(A, B, C))
