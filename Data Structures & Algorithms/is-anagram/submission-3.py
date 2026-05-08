class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        dct = {}

        for c in s:
            dct[c] = dct.get(c, 0) + 1

        for c in t:
            if not dct.get(c):
                return False

            dct[c] -= 1
            if dct[c] < 0:
                return False

        return True
        