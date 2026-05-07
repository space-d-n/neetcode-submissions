class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        running_sub = 0
        max_sub = 0
        seen = {}

        for i in range(len(s)):
            c = s[i]
            if c not in seen:
                running_sub += 1
                seen[c] = i
            else:
                diff = i - seen[c]
                if running_sub >= diff:
                    running_sub = i - seen[c]
                else:
                  running_sub += 1
                seen[c] = i

            if running_sub > max_sub:
                    max_sub = running_sub
            
            print(f"{c}-{running_sub}-{max_sub}")
            # print(seen)
            print()

        return max_sub
