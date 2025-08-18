# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}
        
        def dfs(idx):
            if idx >= n:
                return 0
            if idx in memo:
                return memo[idx]
            p, b = questions[idx]
            memo[idx] = max(
            dfs(idx + 1),
            p + dfs(idx + 1 + b)
            )
            return memo[idx]
        
        return dfs(0)