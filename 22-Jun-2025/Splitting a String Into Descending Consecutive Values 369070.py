# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def helper(idx, prev):
            if idx >= n: return True

            for j in range(idx, n):
                curr = int(s[idx: j+1])
                if prev - curr == 1:
                    if helper(j+1, curr):
                        return True
            return False

        for i in range(1, n):
            curr = int(s[:i])
            if helper(i, curr):
                return True
        return False
        