import sys

int_num = int(sys.stdin.readline())
nums = [0 for i in range(10002)]

for _ in range(int_num):
    nums[int(sys.stdin.readline())] += 1

for i in range(1, len(nums)):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)
