class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if target == nums[0]:
            return 0

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            print(f"{l}-{m}-{r}")

            if (nums[m] == target):
                return m
            elif (nums[l] <= nums[m]):

                if (nums[l] <= target < nums[m]):
                    r = m - 1
                else:
                    l = m + 1
            elif (nums[m] <= nums[r]):

                if (nums[m] < target <= nums[r]):
                    l = m + 1
                else:
                    r = m - 1

        return -1

        return -1