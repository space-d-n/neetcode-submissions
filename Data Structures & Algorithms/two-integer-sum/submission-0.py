class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dict = {}

        for i in range(len(nums)):

            local_target = target - nums[i]
            
            if (nums_dict.get(local_target) is not None):
                return [nums_dict[local_target], i]

            nums_dict[nums[i]] = i
