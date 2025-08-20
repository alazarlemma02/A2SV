# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        i = 0
        while num:
            if (num & 1) == 0:
                res += (1 << i)
            i+=1
            num >>= 1
        return res
        