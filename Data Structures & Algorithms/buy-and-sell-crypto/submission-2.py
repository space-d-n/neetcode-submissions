class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_p = prices[0]
        max_profit = 0

        for i in range(len(prices)):

            profit = prices[i] - min_p
            if profit > max_profit:
                max_profit = profit

            if (prices[i] < min_p):
                min_p = prices[i]

        return max_profit