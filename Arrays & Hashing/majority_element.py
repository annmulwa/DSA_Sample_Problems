# Time complexity: O(n)
# Space complexity: O(n)
def majorityElement(nums):
    hashmap = {}
    res = len(nums) // 2

    for n in nums:
        hashmap[n] = 1 + hashmap.get(n, 0)
        if hashmap[n] > res:
            return n

nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]
print(majorityElement(nums))

# Boyer - Moore Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
def majorityElement1(nums):
    res, count = 0, 0

    for n in nums:
        if count == 0:
            res = n
        count += (1 if n == res else -1)
    return res

nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2]
print(majorityElement1(nums))