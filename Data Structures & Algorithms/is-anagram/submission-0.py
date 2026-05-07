class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_chars = {}
        t_chars = {}

        for i in range(len(s)):
            if s_chars.get(s[i]) is None:
                s_chars[s[i]] = 1
            else:
                s_chars[s[i]] += 1

            if t_chars.get(t[i]) is None:
                t_chars[t[i]] = 1
            else:
                t_chars[t[i]] += 1

        for key in s_chars.keys():
            if t_chars.get(key) == s_chars.get(key):
                continue
            else:
                return False

        return True
                