# Time Complexity: O(n log n + m log m)
# Space Complexity: O(n + m)
def isAnagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    return False

str1 = "racecar"
str2 = "carrace"
print(isAnagram(str1, str2))

# Time Complexity: O(n)
# Space Complexity: O(n)
def isAnagram1(s, t):
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        # print(countS[c])
        if countS[c] != countT.get(c, 0):
            return False
    return True

# str1 = "racecar"
# str2 = "carrace"

str1 = "racecar"
str2 = "carrace"

print(isAnagram1(str1, str2))

from collections import Counter
def isAnagram2(s, t):
    if Counter(s) == Counter(t):
        return True
    return False

str1 = "racecat"
str2 = "carrace"
print(isAnagram1(str1, str2))