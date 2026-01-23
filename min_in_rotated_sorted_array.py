# Problem
# You are given a rotated sorted array of distinct integers.
# Return the minimum element.

# Input
# 4,5,6,7,0,1,2
# Output
# 0

def minimum(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

nums_input = input().strip()
nums = list(map(int, nums_input.replace(" ", "").split(",")))
res = minimum(nums)
print(res)
