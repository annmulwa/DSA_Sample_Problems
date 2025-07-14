# Time Complexity: O(n^2)
# Space Complexity: O(1)
def sortColors(nums):
    if len(nums) <= 1:
        return nums
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        i += 1
    return nums

nums = [2, 1, 0, 1]
print(sortColors(nums))

# using quick sort
# Time Complexity: O(n)
# Space Complexity: O(1)
def sortColors1(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    l = 0
    r = len(nums) - 1
    i = 0

    while i <= r:
        if nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
        elif nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
            i -= 1
        i += 1
    return nums

nums = [2, 1, 0]
print(sortColors1(nums))