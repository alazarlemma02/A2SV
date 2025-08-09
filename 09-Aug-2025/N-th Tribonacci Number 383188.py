# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n < 3:
            return dp[n]

        for i in range(3, n+1):
            curr = sum(dp)
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = curr
        return dp[2]        