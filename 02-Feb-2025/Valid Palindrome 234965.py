# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution(object):
    def isPalindrome(self, s):
        alphanumeric = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        result = []
        for char in s.lower():
            if char in alphanumeric:
                result.append(char)

        result = "".join(result)
        return result == result[::-1]

        