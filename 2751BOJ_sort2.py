import sys

cases = int(input())
nums = []
for _ in range(cases):
    nums.append(int(sys.stdin.readline()))


def mergesort(data):
    if len(data) <= 1:
        return data

    medium = len(data)//2
    left = data[:medium]
    right = data[medium:]

    return insert_sort(mergesort(left), mergesort(right))


def insert_sort(left, right):
    left_length = len(left)
    right_length = len(right)
    if left_length == 0 and right_length == 1:
        return right
    elif left_length == 0 and right_length == 0:
        return []
    else:
        result = []
        i, j = 0, 0
        while i < left_length or j < right_length:
            if i >= left_length:
                result.extend(right[j:])
                break
            elif j >= right_length:
                result.extend(left[i:])
                break
            elif left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result


sortedNums = mergesort(nums)
for i in range(cases):
    sys.stdout.write(str(sortedNums[i]) + '\n')
