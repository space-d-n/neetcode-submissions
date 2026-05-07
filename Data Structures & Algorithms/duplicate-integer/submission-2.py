class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}

        for num in nums:
            if not nums_dict.get(num):
                nums_dict[num] = 0
            nums_dict[num] += 1
            if nums_dict[num] > 1:
                return True

        return False

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen = set()

#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)

#         return False        