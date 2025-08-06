# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        res = []
        res.append([1, 1])
        if rowIndex == 1:
            return res[0]
        
        for i in range(2, rowIndex+1):
            prev = res.pop()
            curr = []
            curr.append(1)
            for j in range(i-1):
                curr.append(prev[j]+prev[j+1])
            curr.append(1)
            res.append(curr)
        return res.pop()

        