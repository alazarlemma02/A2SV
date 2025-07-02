# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # lsit of valid path connections
        unit_vector = {
            1: [(0, 1), (0, -1)],
            2: [(1, 0), (-1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        def dfs(row, col):
            if row == len(grid)-1 and col == len(grid[0])-1:
                return True
            visited[row][col] = 1

            for dx, dy in unit_vector[grid[row][col]]:
                crow, ccol = row+dx, col+dy
                if inbound(crow, ccol) and not visited[crow][ccol] and (-1*dx, -1*dy) in unit_vector[grid[crow][ccol]]:
                    found = dfs(crow, ccol)
                    if found:
                        return True
            return False 

        rl, cl = len(grid), len(grid[0])
        visited = [[0]* cl for _ in range(rl)]
        return dfs(0, 0)

