# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        mismatch_counter = 0
        mismatch = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatch_counter += 1
                mismatch.append(s1[i])
                mismatch.append(s2[i])
        if mismatch_counter == 2:
            if mismatch[0]==mismatch[3] and mismatch[1]==mismatch[2]:
                return True
        return False


         
            

        