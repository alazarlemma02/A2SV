# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rl, cl = len(matrix), len(matrix[0])
        self.prex_matrix = [[0] * (cl+1) for _ in range(rl+1)]
        for row in range(rl):
            prex_sum = 0
            for col in range(cl):
                prex_sum += matrix[row][col]
                above = self.prex_matrix[row][col+1]
                self.prex_matrix[row+1][col+1] = prex_sum + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        br = self.prex_matrix[row2+1][col2+1]
        above = self.prex_matrix[row1][col2+1]
        left = self.prex_matrix[row2+1][col1]
        tl = self.prex_matrix[row1][col1]
        return br - above - left + tl
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)