class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique = set(nums)

        max_cnt = 0
        for num in unique:
            if num - 1 not in unique:
                current = num
                cnt = 0
                while current in unique:
                    current += 1
                    cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt

        return max_cnt

        
            