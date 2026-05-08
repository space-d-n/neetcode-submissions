class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dct = {}

        for num in nums:

            dct[num] = dct.get(num, 0) + 1
            if dct[num] > 1:
                return True
        
        return False
