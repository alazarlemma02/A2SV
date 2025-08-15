# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[[-1 for _ in range(2)] for _ in range(3)] for _ in range(n+1)]
        def dfs(day, tr, buy):
            if day >= n or tr == 0:
                return 0
            
            if dp[day][tr][buy] != -1:
                return dp[day][tr][buy]

            if buy:
                sell = prices[day] + dfs(day+1, tr-1, not buy)
                not_sell = dfs(day+1, tr, buy)
                dp[day][tr][buy] = max(sell, not_sell)
                return dp[day][tr][buy]
            else:
                buyy = dfs(day+1, tr, not buy) - prices[day]
                not_buy = dfs(day+1, tr, buy)
                dp[day][tr][buy] = max(buyy, not_buy)
                return dp[day][tr][buy]
        
        return dfs(0, 2, 0)



