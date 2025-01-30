# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        rev = str(x)[::-1]
        return str(x)==rev
        