# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        memo = {}
        
        def dfs(i, match_cnt):
            if match_cnt == len(s):
                return True
            if i == len(t):              
                return False

            if (i, match_cnt) in memo:
                return memo[(i, match_cnt)]
             
            take = False
            if t[i] == s[match_cnt]:
                take = dfs(i+1, match_cnt+1)

            not_take = dfs(i+1, match_cnt)
            memo[(i, match_cnt)] = take or not_take
            return memo[(i, match_cnt)]

        return dfs(0, 0)
