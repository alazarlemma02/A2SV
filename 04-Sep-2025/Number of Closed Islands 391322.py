# Problem: Number of Closed Islands - https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rl, cl = len(grid), len(grid[0])
        visited = [[0] * cl for _ in range(rl)]
        
        def dfs(row, col):
            if row < 0 or row >= rl or col < 0 or col >= cl:
                return False
            if grid[row][col] == 1 or visited[row][col]:
                return True
            visited[row][col] = 1

            up = dfs(row-1, col)
            left = dfs(row, col-1)
            bottom = dfs(row+1, col)
            right = dfs(row, col+1)
            
            return up and left and bottom and right

        cnt = 0
        for row in range(rl):
            for col in range(cl):
                if grid[row][col] == 0 and not visited[row][col]:
                    if dfs(row, col):
                        cnt +=1
        return cnt