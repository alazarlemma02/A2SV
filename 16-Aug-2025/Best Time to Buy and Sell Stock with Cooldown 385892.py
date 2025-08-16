# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
    
        def dfs(i, holding):
            if i >= n:
                return 0

            if (i, holding) in memo:
                return memo[(i, holding)]
            
            if holding == 0:
                buy = -prices[i] + dfs(i+1, 1)
                skip = dfs(i+1, 0)
                memo[(i, holding)] = max(buy, skip)
                return memo[(i, holding)]
            else:
                sell = prices[i] + dfs(i+2, 0)
                hold = dfs(i+1, 1)
                memo[(i, holding)] = max(sell, hold)
                return memo[(i, holding)]
        
        return dfs(0, 0)