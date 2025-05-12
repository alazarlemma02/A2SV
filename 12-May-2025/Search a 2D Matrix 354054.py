# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl, cl = len(matrix), len(matrix[0])

        for row in range(rl):
            left, right = 0, cl
            while left < right:
                mid = (right + left) // 2
                if matrix[row][mid] == target:
                    return True
                if matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid
        return False
            