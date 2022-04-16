import sys

cases = list(map(int, sys.stdin.readline().split(' ')))
nums = list(map(int, sys.stdin.readline().split(' ')))


nums.sort()
print(nums[cases[1]-1])
