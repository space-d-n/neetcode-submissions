class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        current_profit = 0

        for i in range(1, len(prices), 1):

            day_profit = prices[i] - prices[i - 1]

            current_profit += day_profit
            max_profit = max(max_profit, current_profit)
            current_profit = max(current_profit, 0)

        return max_profit

