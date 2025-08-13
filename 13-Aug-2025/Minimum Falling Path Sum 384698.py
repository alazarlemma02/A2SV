# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rl, cl = len(matrix), len(matrix[0])
        min_sum = float('inf')
        memo = {}

        def dfs(row, col):
            if col < 0 or col >= cl:
                return float('inf')
            if row == rl:
                return 0
            if (row, col) in memo:
                return memo[(row, col)]

            total = matrix[row][col] + min(dfs(row+1, col-1), dfs(row+1, col), dfs(row+1, col+1))
            memo[(row, col)] = total
            return total

        for col in range(cl):
            min_sum = min(min_sum, dfs(0, col))
        return min_sum

        