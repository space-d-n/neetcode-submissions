class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        max_freq = 0
        seen = {}
        ans = 0

        for r, c in enumerate(s):

            print(f"{l}-{r}")
            print(f"{(r - l + 1) - max_freq}")

            seen[c] = seen.get(c, 0) + 1
            max_freq = max(max_freq, seen[c])

            if (r - l + 1) - max_freq > k:
                seen[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)
        
        return ans