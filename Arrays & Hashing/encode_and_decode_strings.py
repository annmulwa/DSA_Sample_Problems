# Time complexity: O(n) where n is the number of characters in a string
# Space complexity: O(n) where n is the number of characters in a string
def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(s):
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        res.append(s[j + 1:j + 1 + length])
        i = j + 1 + length
    return res

strs = ["neet", "co#de"]
strs_encode = encode(strs)
print(encode(strs))
print(decode(strs_encode))