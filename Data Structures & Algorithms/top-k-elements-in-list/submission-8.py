class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_freq = {}

        # count frequencies of nums
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        print(num_freq)

        # create list of buckets/lists indexed by frequency
        # max(possible buckets) = len(nums)
        buckets = [[] for _ in range(len(nums))]
        print(buckets)
        for num, freq in num_freq.items():
            print(f"{num}-{freq}")
            buckets[freq - 1].append(num)
            print(buckets)

        # go through nums in buckets until getting k nums
        top_k = []
        print(top_k)
        for i in range(len(buckets) - 1, -1, -1):
            print(i)
            for num in buckets[i]:
                top_k.append(num)
                print(top_k)
                if len(top_k) == k:
                    return top_k