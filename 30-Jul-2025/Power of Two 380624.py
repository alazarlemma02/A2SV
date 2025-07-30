# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        while n >= 2 and n % 2 == 0:
            n //= 2
        return True if n == 1 else False
