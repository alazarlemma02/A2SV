# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """     
        Do not return anything, modify matrix in-place instead.
        """
        rl, cl = len(matrix), len(matrix[0])
        zero_row, zero_col = [], []

        for row in range(rl):
            for col in range(cl):
                if matrix[row][col] == 0:
                    zero_row.append(row)
                    zero_col.append(col)
        
        for zr in zero_row:
            for col in range(cl):
                matrix[zr][col] = 0
        for cr in zero_col:
            for row in range(rl):
                matrix[row][cr] = 0