# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c**0.5)

        while left <= right:
            curr = left**2 + right**2
            if curr == c:
                return True
            if curr > c:
                right -=1
            else:
                left +=1
        return False
