# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rl, cl = len(grid), len(grid[0])
        visited = [[0]*cl for _ in range(rl)]

        def dfs(row, col):
            if row < 0 or row >= rl or col < 0 or col >= cl or not grid[row][col]:
                return 1
            
            if visited[row][col]:
                return 0

            visited[row][col] = 1

            count = dfs(row-1, col)
            count += dfs(row, col-1)
            count += dfs(row+1, col)
            count += dfs(row, col+1)

            return count

        for row in range(rl):
            for col in range(cl):
                if grid[row][col]:
                    return dfs(row, col)