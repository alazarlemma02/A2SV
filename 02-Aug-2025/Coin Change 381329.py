# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {0:0}

        def dfs(amount):
            if amount in memo:
                return memo[amount]
            
            min_coin = float('inf')
            for coin in coins:
                curr = amount - coin
                if curr < 0:
                    break     
                min_coin = min(min_coin, 1 + dfs(curr))  

            memo[amount] = min_coin
            return min_coin

        res = dfs(amount)
        return res if res != float('inf') else -1