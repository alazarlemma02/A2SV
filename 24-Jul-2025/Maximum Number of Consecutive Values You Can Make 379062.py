# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        curr = 0

        for coin in coins:
            if curr + 1 < coin:
                return curr + 1
            curr += coin
        return curr + 1