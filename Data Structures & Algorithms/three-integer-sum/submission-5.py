class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        triplets = set()
        print(nums)
        
        for j in range(1, len(nums) - 1, 1):

            i = 0
            k = len(nums) - 1
            while i < j and j < k:

                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
                    i += 1

                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] <0:
                    i += 1

        
        return [[t[0],t[1],t[2]] for t in triplets]

        # triplets = set()
        # for x in range(2, len(nums), 1):
        #     if nums[i] + nums[j] + nums[k] == 0:
        #         triplets.add((nums[i], nums[j], nums[k]))
        # k = 
        
        # for j in range(1, len(nums), 1):
        #     if nums[i] + nums[j] + nums[k] == 0:
        #         triplets.add((nums[i], nums[j], nums[k]))