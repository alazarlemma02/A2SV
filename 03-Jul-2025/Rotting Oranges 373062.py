# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque()
        forg = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    forg += 1
        
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        mint = 0
        
        while queue:
            r, c, mint = queue.popleft()
            
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    grid[nr][nc] = 2 
                    forg -= 1
                    queue.append((nr, nc, mint + 1))
        
        return mint if forg == 0 else -1
