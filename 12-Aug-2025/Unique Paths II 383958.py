# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or obstacleGrid[row][col] == 1:
                return 0
            if row == m-1 and col == n-1:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            
            cnt = dfs(row + 1, col) + dfs(row, col+1)
            memo[(row, col)] = cnt
            return cnt

        return dfs(0, 0)