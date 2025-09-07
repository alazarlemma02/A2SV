# Problem: Reverse Bits - https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while i < 32: 
            curr = (n >> i) & 1
            res |= (curr << (31 - i))
            i +=1
        return res
        