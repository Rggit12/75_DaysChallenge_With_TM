class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = -math.inf
        buy = prices[0]
        
        for i in prices:
            max_profit = max(max_profit,i-buy)
            buy = min(buy,i)
        return max_profit
           