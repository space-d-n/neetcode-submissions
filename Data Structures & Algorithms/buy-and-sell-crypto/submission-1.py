class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_p = prices[0]

        diff = [0] * len(prices)

        for i in range(len(prices)):

            diff[i] = prices[i] - min_p

            if (prices[i] < min_p):
                min_p = prices[i]

        print(diff)

        return max(diff)