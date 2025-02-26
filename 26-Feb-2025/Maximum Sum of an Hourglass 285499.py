# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        rl,cl = len(grid), len(grid[0])
        
        for row in range(rl-2):
            for col in range(cl-2):
                curr_sum = sum(grid[row][col:col+3]) + grid[row+1][col+1] + sum(grid[row+2][col:col+3])
                max_sum = max(max_sum, curr_sum)
                    
        return max_sum
                