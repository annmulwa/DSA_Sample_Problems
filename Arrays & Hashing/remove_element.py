# Time complexity: O(n)
# Space complexity: O(n)
def removeElement(nums, val):
    ans = []
    res = 0
    for n in nums:
        if n != val:
            ans.append(n)
            res += 1
    return ans, res

nums = [1, 1, 2, 3, 4, 4]
val = 1
print(removeElement(nums, val))

# Time complexity: O(n)
# Space complexity: O(1)
def removeElement1(nums, val):
    res = 0

    for n in nums:
        if n != val:
            res += 1
    return res

nums = [1, 1, 2, 3, 4, 4]
val = 1
print(removeElement1(nums, val))

# Correct code-(doing it in-place)
# Time complexity: O(n)
# Space complexity: O(1)
def removeElement2(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [1, 2, 3, 4, 4]
val = 4
print(removeElement2(nums, val))
