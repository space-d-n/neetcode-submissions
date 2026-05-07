class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # if (len(nums) == 1 ):
        #     if (nums[0])
        #     return nums[0]

        if target == nums[0]:
            return 0

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            print(f"{l}-{m}-{r}")

            if (nums[m] == target):
                return m
            elif (nums[m] < target and target >= nums[0]):
                if (nums[m] >= nums[0]):
                    l = m + 1
                else:
                    r = m - 1
            elif (nums[m] < target and target < nums[0]):
                l = m + 1
            elif (nums[m] > target and target < nums[0]):
                if (nums[m] >= nums[0]):
                    l = m + 1
                else:
                    r = m - 1
            elif (nums[m] > target and target >= nums[0]):
                r = m - 1

        return -1