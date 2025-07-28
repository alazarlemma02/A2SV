# Problem: Delete Columns to Make Sorted - https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rl, cl = len(strs), len(strs[0])
        cnt = 0

        for col in range(cl):
            curr = []
            for row in range(rl):
                if curr and curr[-1] > strs[row][col]:
                    cnt +=1
                    break
                curr.append(strs[row][col])

        return cnt