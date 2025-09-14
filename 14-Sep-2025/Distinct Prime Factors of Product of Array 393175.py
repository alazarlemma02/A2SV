# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set()
        for num in nums:
            curr = 2
            while curr * curr <= num:
                while num % curr == 0:
                    num //= curr
                    res.add(curr)
                curr += 1
            if num > 1:
                res.add(num)
        return len(res)