# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rl, cl = len(matrix), len(matrix[0])

        for row in range(1,rl):
            for col in range(1,cl): 
                if matrix[row][col] != matrix[row-1][col-1]:
                    return False        
        return True



