# Time Complexity: O(n)
# Space Complexity: O(n)
def getConcatenation(nums):
    nums_dup = []
    for i in range(len(nums)):
        nums_dup.append(nums[i])
    return nums + nums_dup

nums = [1, 4, 1, 2]
print(getConcatenation(nums))

def getConcatenation1(nums):
    return nums + nums

nums = [1, 4, 1, 2]
print(getConcatenation1(nums))

def getConcatenation2(nums):
    ans = []
    for i in range(2):
        for n in nums:
            ans.append(n)
    return ans

nums = [1, 4, 1, 2]
print(getConcatenation2(nums))
