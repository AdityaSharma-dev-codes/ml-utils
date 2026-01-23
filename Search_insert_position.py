# Problem
# Given a sorted array and a target, return the index if found.
# If not, return the index where it would be inserted.

# ex:
# Input:
# 1,3,5,6
# 2
# Output:
# 1

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2 # mid will be rounded off to nearest int
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

nums_input = input("Enter sorted numbers: ").strip()
target = int(input().strip())
nums = list(map(int, nums_input.replace(" ", "").split(",")))

# nums_input = input("enter sorted numbers")
# nums = {int(x) for x in nums_input.replace(',', '')}

res = search(nums, target)
print(res)