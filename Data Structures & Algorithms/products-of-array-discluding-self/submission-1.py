class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)

        running_prod = 1
        for i in range(0, len(nums) - 1, 1):
            running_prod *= nums[i]
            result[i+1] *= running_prod

        running_prod = 1
        for i in range(len(nums) - 1, 0, -1):
            running_prod *= nums[i]
            result[i - 1] *= running_prod

        return result
