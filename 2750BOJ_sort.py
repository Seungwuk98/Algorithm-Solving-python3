import sys

sys.setrecursionlimit(99999)

cases = int(input())
nums = list()
for _ in range(cases):
    nums.append(int(input()))


def quicksort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [i for i in data[1:] if i < pivot]
    right = [i for i in data[1:] if i > pivot]

    return quicksort(left) + [pivot] + quicksort(right)


sorted = quicksort(nums)
for i in range(len(sorted)):
    print(sorted[i])
