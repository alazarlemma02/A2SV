# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """     
        Do not return anything, modify matrix in-place instead.
        """
        rl, cl = len(matrix), len(matrix[0])
        idx_set = set()

        for row in range(rl):
            for col in range(cl):
                if matrix[row][col] == 0:
                    idx_set.add((row,col))

        for row in range(rl):
            for col in range(cl):
                if (row,col) in idx_set:
                    r, c = 0, 0
                    while r < rl:
                        matrix[r][col] = 0
                        r +=1
                    while c < cl:
                        matrix[row][c] = 0
                        c +=1                  
                   