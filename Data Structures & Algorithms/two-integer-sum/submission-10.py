class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dct = {}

        for (i, num) in enumerate(nums):
            print(dct)
            diff = target - num
            print(diff)

            if dct.get(diff) is not None:
                print(dct.get(diff))
                return [dct[diff], i]
            else:
                dct[num] = i