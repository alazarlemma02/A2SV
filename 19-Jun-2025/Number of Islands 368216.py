# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rl, cl = len(grid), len(grid[0])
        visited = [[0]*cl for _ in range(rl)]

        def dfs(row, col):
            if row < 0 or row >= rl or col < 0 or col >= cl:
                return
            if grid[row][col] == "0" or visited[row][col]:
                return
            
            visited[row][col] = 1
            top = dfs(row-1, col)
            left = dfs(row, col-1)
            bottom = dfs(row+1, col)
            right = dfs(row, col+1)

        count = 0

        for row in range(rl):
            for col in range(cl):
                if grid[row][col] != "0" and not visited[row][col]:
                    dfs(row, col)
                    count +=1
        return count