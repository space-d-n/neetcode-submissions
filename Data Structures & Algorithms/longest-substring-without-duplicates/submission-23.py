class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        max_len = 0
        seen = {}

        for r, c in enumerate(s):

            if (c in seen) and seen[c] >= l:
                l = seen[c] + 1

            seen[c] = r

            max_len = max(max_len, r - l + 1)

        return max_len


        # Harder to reason (my initial solution)
        # running_sub = 0
        # max_sub = 0
        # seen = {}

        # for i in range(len(s)):
        #     c = s[i]
        #     if c not in seen:
        #         running_sub += 1
        #         seen[c] = i
        #     else:
        #         diff = i - seen[c]
        #         if running_sub >= diff:
        #             running_sub = i - seen[c]
        #         else:
        #           running_sub += 1
        #         seen[c] = i

        #     if running_sub > max_sub:
        #             max_sub = running_sub

        # return max_sub
