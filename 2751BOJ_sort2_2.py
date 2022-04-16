import sys

cases = int(input())
nums = []
for _ in range(cases):
    nums.append(int(sys.stdin.readline()))

nums.sort()

for i in range(cases):
    sys.stdout.write(str(nums[i]) + '\n')
