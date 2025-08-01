# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 0
            if row == m-1 and col == n-1:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            
            cnt = dfs(row + 1, col) + dfs(row, col+1)
            memo[(row, col)] = cnt
            return cnt

        return dfs(0, 0)