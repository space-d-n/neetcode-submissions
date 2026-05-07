class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        chars1 = {}
        chars2 = {}
        for s1, t1 in zip(s, t):
            chars1[s1] = chars1.get(s1, 0) + 1
            chars2[t1] = chars2.get(t1, 0) + 1

        return chars1 == chars2

# Pythonic, readable
# def isAnagram(self, s: str, t: str) -> bool:
#     return Counter(s) == Counter(t)

# One dictionary
# def isAnagram(self, s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False

#     count = {}

#     for c in s:
#         count[c] = count.get(c, 0) + 1

#     for c in t:
#         if c not in count:
#             return False
#         count[c] -= 1
#         if count[c] == 0:
#             del count[c]

#     return not count