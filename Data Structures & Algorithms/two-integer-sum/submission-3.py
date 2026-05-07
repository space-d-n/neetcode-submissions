class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        difference = {}

        for i, value in enumerate(nums):

            if difference.get(target - nums[i]) != None:
                return [difference[target - nums[i]], i]
            else: 
                difference[nums[i]] = i

        return []