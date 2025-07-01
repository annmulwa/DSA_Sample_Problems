# Time Complexity: O(n²)
# Space Complexity: O(1)
def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

nums = [3,4]
target = 7
print(twoSum(nums, target))

# Hashmap(two pass)
# Time Complexity: O(n)
# Space Complexity: O(n)
def twoSum1(nums, target):
    hashmap = {}

    for i, n in enumerate(nums):
        hashmap[n] = i

    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashmap and hashmap[diff] != i:
            return [i, hashmap[diff]]
    return []

nums = [2, 1, 5, 3]
target = 4
print(twoSum1(nums, target))

# Hashmap(one pass)
# Time Complexity: O(n)
# Space Complexity: O(n)
def twoSum2(nums, target):
    hashmap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[n] = i

nums = [2, 1, 5, 3]
target = 4
print(twoSum2(nums, target))
