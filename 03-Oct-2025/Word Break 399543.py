# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = 0
        for word in wordDict:
            max_len = max(max_len, len(word))

        dp = [False] * (len(s)+1)
        dp[0] = True

        for i in range(1, len(s)+1):
            j = i - 1
            while j >= max(0, i-max_len):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
                j -=1
        return dp[-1]
