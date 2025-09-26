# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        left = 0
        total = sum(map(int, list(s)))
        for i in range(len(s)-1):
            if s[i] == "0":
                left +=1
            else:
                total -= 1
            res = max(res, left + total)
        return res