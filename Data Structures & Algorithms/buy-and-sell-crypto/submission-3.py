class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for R in range(len(prices)):
            if prices[R] < min_price:
                min_price = prices[R]
            max_profit = max(max_profit, prices[R] - min_price)
        return max_profit

            


