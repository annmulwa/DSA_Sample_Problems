# Time complexity: O(n * k log k)
# Space complexity: O(n * k)
from collections import defaultdict
def groupAnagrams(strs):
    hashmap = defaultdict(list)

    for s in strs:
        str_sorted = sorted(s)
        strS = ('').join(str_sorted)
        hashmap[strS].append(s)
    return list(hashmap.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))

# Time complexity: O(n * k)
# Space complexity: O(n * k)
def groupAnagrams1(strs):
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26   # a -> z
        # print(count)

        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return list(res.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams1(strs))