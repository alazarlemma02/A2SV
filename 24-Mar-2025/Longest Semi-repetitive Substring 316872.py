# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)

        max_rep = i = last = prev = rep_count = 0

        
        for j in range(n):
            if s[j] == s[j-1]:
                prev = last
                last = j
                rep_count +=1

            if rep_count > 1:
                rep_count -=1
                i = prev

            max_rep = max(max_rep, j - i + 1)

        return max_rep
        