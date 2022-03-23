class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        max_profit = 0
        
        left = 0 
        right = 1
        
        while right < len(prices):
            profit = prices[right] - prices[left] 
            if prices[left] < prices[right]:
                max_profit = max(profit, max_profit)
                
            else:
                left = right
            right += 1
            
        return max_profit
                
                            