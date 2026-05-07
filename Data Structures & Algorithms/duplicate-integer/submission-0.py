class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        chars = {}

        for num in nums:
            if chars.get(num) is None:
                chars[num] = 1
            else:
                chars[num] += 1
            if chars[num] > 1:
                return True

        return False