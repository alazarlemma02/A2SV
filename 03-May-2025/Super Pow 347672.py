# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        if a == 1 or b == 0:
            return 1

        b = int("".join(map(str, b)))

        def pow(a, b, MOD):
            if b == 0:
                return 1
            if b % 2 == 0:
                res = pow(a, b//2, MOD)
                return (res * res) % MOD
            return (a * pow(a, b-1, MOD)) % MOD

        return pow(a, b, MOD) % MOD   
        