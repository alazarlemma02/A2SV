# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while (mask & b) > 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return mask & a if b > 0 else a
        