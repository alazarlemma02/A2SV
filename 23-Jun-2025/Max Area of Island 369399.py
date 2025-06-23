# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rl, cl = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rl or col < 0 or col >= cl:
                return 0

            if grid[row][col] != 1:
                return 0
            grid[row][col] = 2

            isl_area = 1 + dfs(row-1, col) + dfs(row, col-1) + dfs(row+1, col) + dfs(row, col+1)
            return isl_area

        for row in range(rl):
            for col in range(cl):
                if grid[row][col]:
                    max_area = max(max_area, dfs(row, col))
        return max_area