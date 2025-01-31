# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution(object):
    def reverseString(self, s):
        left, right = 0, len(s)-1
        while left < right:
            current = s[left]
            s[left] = s[right]
            s[right] = current
            left +=1
            right -=1
        return s
        