# Problem: Append Characters to String to Make Subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        
        i, j = 0, 0

        while i < n and j < m:
            if s[i] == t[j]:
                j +=1
            i +=1
        return m - j

        