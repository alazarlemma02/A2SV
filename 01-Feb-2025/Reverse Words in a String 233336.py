# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -=1
        result = ' '.join(s)
        return result
        