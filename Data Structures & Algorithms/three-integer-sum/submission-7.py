class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        triplets = set()
        print(nums)
        
        for i in range(len(nums) - 2):
            print(i)

            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:

                print(f"i - {i}, j - {j}, k - {k}")
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1

        
        return [[t[0],t[1],t[2]] for t in triplets]