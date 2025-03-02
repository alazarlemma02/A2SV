# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        rl, cl = len(matrix), len(matrix[0])

        maximum = 0
        minn = abs(matrix[0][0])
        count = 0

        for row in range(rl):
            for col in range(cl):
                maximum += abs(matrix[row][col])
                minn = min(minn, abs(matrix[row][col]))
                if matrix[row][col] < 0: count +=1
        
        return maximum- (2*minn) if count % 2 != 0 else maximum

                    
                
        