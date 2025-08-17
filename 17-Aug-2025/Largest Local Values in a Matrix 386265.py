# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rl, cl = len(grid), len(grid[0])
        res = [[0 for _ in range(cl-2)] for _ in range(rl-2)]
        

        for row in range(rl-2):
            for col in range(cl-2):
                for r in range(row, row+3):
                    for c in range(col, col+3):
                        res[row][col] = max(res[row][col], grid[r][c])
        return res


        