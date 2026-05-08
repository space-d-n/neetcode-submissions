class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dct = {}

        for (i, num) in enumerate(nums):
            diff = target - num

            if dct.get(diff) is not None:
                return [dct[diff], i]
            
            dct[num] = i