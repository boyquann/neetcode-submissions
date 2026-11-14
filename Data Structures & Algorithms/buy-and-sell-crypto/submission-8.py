class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            max_price = max(max_price, prices[i] - min_price)
        return max_price if max_price > 0 else 0


