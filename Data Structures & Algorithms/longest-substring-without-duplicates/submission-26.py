class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        max_len = 0
        seen = {}

        for r, c in enumerate(s):

            if c in seen and seen[c] >= l:
                l = seen[c] + 1

            seen[c] = r
            max_len = max(max_len, r - l +1)
            print(max_len)
        
        return max_len