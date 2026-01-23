# Problem

# Every element appears twice except one.
# Find that single element in O(log n) time.

# Input
# 1,1,2,3,3,4,4,8,8

# Output
# 2

def single_element_search(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2

        if nums[mid] == nums[mid + 1]:
            left = mid + 2
            # print(f"left: {left},  {nums[left]}")
        else:
            right = mid
            # print(f"right: {right}, {nums[right]}")
        # print(f"mid: {mid}, {nums[mid]}")

    return nums[left]

nums_input = input("Enter the list: ").strip()
nums = list(map(int, nums_input.replace(" ", "").split(",")))

res = single_element_search(nums)
print(res)