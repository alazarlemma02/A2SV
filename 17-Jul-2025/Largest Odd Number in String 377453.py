# Problem: Largest Odd Number in String - https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        right = n-1
        while right >= 0:
            if int(num[right]) % 2 == 1:
                return num[:right+1]
            right -=1
        return ""

        