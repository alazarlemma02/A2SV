# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        buy_price = prices[0]
        profit = 0
        for price in prices[1:]:
            if price < buy_price:
                buy_price = price
            else:
                profit = max(profit, price - buy_price)
        return profit
        
        
            
        
        
        
        
       
        