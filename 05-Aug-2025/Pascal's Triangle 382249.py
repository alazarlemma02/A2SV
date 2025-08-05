# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows == 0:
            return res
        res.append([1])
        if numRows == 1:
            return res

        for i in range(1, numRows):
            prev = res[i-1]

            curr = []
            curr.append(1)
            for j in range(i-1):
                curr.append(prev[j] + prev[j+1])
            curr.append(1)

            res.append(curr)
        return res