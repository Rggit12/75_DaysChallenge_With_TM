class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit, curr_Profit = 0,0
        buy, sell = 0, 0
        while sell<len(prices):
            if prices[sell]-prices[buy]>curr_Profit:
                curr_Profit = prices[sell]-prices[buy]
                sell += 1
            else:
                profit += curr_Profit
                curr_Profit = 0
                buy, sell = sell, sell+1
        profit += curr_Profit
        return profit