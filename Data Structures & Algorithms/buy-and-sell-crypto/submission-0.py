class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            cost_price = prices[i]
            for j in range(len(prices)):
                if j > i:
                    sale_price = prices[j]
                    profit = sale_price - cost_price
                    if profit > max_profit:
                        max_profit = profit
        return max_profit
        