# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * (len(s)+1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        else:
            dp[1] = 0

        for i in range(2, len(s)+1):
            cur = 0
            if s[i-1] != '0':
                cur += dp[i-1]
            num = s[i-2:i] 
            if num[0] != '0' and int(num) <= 26:
                cur += dp[i-2]
            dp[i] = cur
        return dp[-1]
            

        