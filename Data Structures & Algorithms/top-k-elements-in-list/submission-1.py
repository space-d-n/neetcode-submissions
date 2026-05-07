class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        print(counts)

        # Buckets indexed by frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            buckets[freq].append(num)
        print(buckets)

        result = []

        # TODO do with a heap as well
        # Traverse from highest frequency to lowest
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                print(f"freq - {freq}, num - {num}")
                result.append(num)
                if len(result) == k:
                    return result
            

# Naive approach with sorting 
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
    #     counts = {}

    #     for num in nums:
    #         counts[num] = counts.get(num, 0) + 1

    #     sorted_counts = sorted(counts.items(), key = lambda x: x[1])
    #     return [num for num, value in sorted_counts[-k:]]