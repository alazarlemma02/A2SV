# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rl, cl = len(matrix), len(matrix[0])

        l,r= 0, rl-1
        while l < r:
            for i in range(r-l):
                t, b = l, r
                temp = matrix[t][l+i]
                matrix[t][l+i] = matrix[b-i][l]
                matrix[b-i][l] = matrix[b][r-i]
                matrix[b][r-i] = matrix[t+i][r]
                matrix[t+i][r] = temp
            l +=1
            r -=1
        


        