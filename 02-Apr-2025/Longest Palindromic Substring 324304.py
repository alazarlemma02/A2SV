# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1: return s

        res = ""
        for i in range(1, n):
            left, right = i, i

            while s[left] == s[right]:
                left -=1
                right +=1
                if left==-1 or right == n: break

            pal = s[left+1:right]
            if len(pal) > len(res):
                res = pal

            left = i-1
            right = i

            while s[left] == s[right]:
                left -=1
                right +=1

                if left==-1 or right==n: break

            pal = s[left+1:right]
            if len(pal) > len(res):
                res = pal
        return res
        