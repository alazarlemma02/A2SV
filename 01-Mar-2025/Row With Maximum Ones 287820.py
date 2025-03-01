# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        rl, cl = len(mat), len(mat[0])

        maximum = [0,0]
        for row in range(rl):
            count = 0
            for col in range(cl):
                if mat[row][col] == 1:
                    count +=1
            if maximum[1] == count:
                maximum[0] = min(maximum[0], row)
                maximum[1] = count
            else:
                if maximum[1] < count:
                    maximum[0] = row
                    maximum[1] = count

        return maximum

        