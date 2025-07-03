# Time complexity: O(n * m)
# Space complexity: O(m)
"""
Where:
n = number of strings in the input list
m = length of the shortest string (or length of the common prefix in the worst case)
"""
def longestCommonPrefix(strs):
    res = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res


strs = ["bat","bag","bank","band"]
print(longestCommonPrefix(strs))