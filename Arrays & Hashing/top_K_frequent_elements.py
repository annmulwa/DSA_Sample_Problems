# Time complexity: O(n + m log m)
# Space complexity: O(m) (where n = len(nums) and m = number of unique elements)
def topKFrequent(nums, k):
    hashmap = {}
    for i in nums:
        hashmap[i] = 1 + hashmap.get(i, 0)
    map = hashmap.items()
    print(hashmap.items())
    sorted_items = sorted(map, key=lambda item: item[1], reverse=True)
    print(sorted_items)
    return [item[0] for item in sorted_items[:k]]

nums = [1,1,1,2,2,3,3,3,3]
k = 2
print(topKFrequent(nums, k))
