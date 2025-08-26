# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rem = 0
        res = ""
        na = len(a)
        nb = len(b)
        a, b = a[::-1], b[::-1]

        for i in range(max(na, nb)):
            curr_a = a[i] if i < na else 0
            curr_b = b[i] if i < nb else 0

            total = int(curr_a)+int(curr_b) + rem
            res = str(total % 2) + res
            rem = total//2
        if rem:
            res = str(rem) + res
        return res


        