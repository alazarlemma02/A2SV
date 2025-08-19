# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        curr = 1

        for i in range(1, n+1):
            if curr * 2 == i:
                curr = i
            res[i] = 1 + res[i-curr]

        return res

        