class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        r =  len(nums) - 1

        min_m = None
        while l <= r:

            m = (l + r) // 2
            print(f"{l}-{m}-{r}")

            if (nums[m] >= nums[0]):
                l = m + 1
            elif((nums[m] < nums[0])):
                r = m - 1

        if nums[l] < nums[0]:
            return nums[l]
        else:
            return nums[l+1]