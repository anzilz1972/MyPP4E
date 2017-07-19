import sys
lines = sys.stdin.readlines()
nums = [int(x) for x in lines]
nums.sort()
for num in nums:print(num)
