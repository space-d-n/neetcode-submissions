class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        triplets = set()
        # print(nums)
        
        for i in range(len(nums) - 2):
            # print(i)

            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:

                sum3 = nums[i] + nums[j] + nums[k]
                # print(f"i - {i}, j - {j}, k - {k}")
                if sum3 == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                # more optimal first if
                # if s == 0:
                #     res.append([nums[i], nums[j], nums[k]])
                #     j += 1
                #     k -= 1

                #     while j < k and nums[j] == nums[j - 1]:
                #         j += 1
                #     while j < k and nums[k] == nums[k + 1]:
                #         k -= 1
                elif sum3 > 0:
                    k -= 1
                elif sum3 < 0:
                    j += 1

        
        return [[t[0],t[1],t[2]] for t in triplets]