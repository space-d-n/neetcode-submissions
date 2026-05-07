class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if (len(s1) > len(s2)):
            return False

        s1_counts = [0] * 26

        for c in s1:
            pos = ord(c) - ord('a')
            s1_counts[pos] += 1

        s2_counts = [0] * 26
        l = 0
        running_count = 0
        for r, c in enumerate(s2):

            pos_r = ord(c) - ord('a')
            s2_counts[pos_r] += 1

            if r >= len(s1) - 1:

                if s1_counts == s2_counts:
                    return True

                pos_l = ord(s2[l]) - ord('a')
                s2_counts[pos_l] -= 1
                l += 1

        return False
