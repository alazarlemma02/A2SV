# Problem: Find the Index of the First Occurrence in a String - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)

        i = 0
        j = n-1
        while j < len(haystack):
            if haystack[i:j+1] == needle:
                return i
            i +=1
            j +=1
        return -1