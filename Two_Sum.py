# Two Sum (Indexes) — Hashing
# Problem
# Given an array and a target, return the indexes of two numbers that add up to the target.

# Input
# 2,7,11,15
# 9
# Output
# 0,1

def two_sums(nums, target):
    seen = {}
    for i, num in enumerate(nums):

        # print(f"{i} {num}")
        complement = target - num

        if complement in seen:
            return seen[complement], i

        seen[num] = i

# nums = list(map(int, input().split(',')))
# target = int(input())

nums_input = input("Enter sorted numbers: ").strip()
target = int(input().strip())
nums = list(map(int, nums_input.replace(" ", "").split(",")))

print(two_sums(nums, target))