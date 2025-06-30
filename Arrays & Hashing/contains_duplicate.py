# Time Complexity: O(n²)
# Space Complexity: O(n)
def hasDuplicate(nums):
    nums_dup = []
    for n in nums:
        if n in nums_dup:
            return True
        nums_dup.append(n)
    return False

nums = [1, 2, 3, 4]
print(hasDuplicate(nums))

# Time Complexity: O(n)
# Space Complexity: O(n)
def hasDuplicate1(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

nums = [1, 2, 3, 3]
print(hasDuplicate1(nums))