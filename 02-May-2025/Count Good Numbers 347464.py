# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10**9 + 7)
        nf_fours = n // 2
        nf_fives = n - nf_fours

        def pow(x, n, MOD):
            if n == 0:
                return 1
            
            if n % 2 == 0:
                res = pow(x, n//2, MOD)
                return (res * res) % MOD
            
            return (x * pow(x, n-1, MOD)) % MOD

        return (pow(5, nf_fives, MOD) * pow(4, nf_fours, MOD)) % MOD
        