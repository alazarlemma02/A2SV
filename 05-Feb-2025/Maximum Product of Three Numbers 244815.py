# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        if len(nums) == 3:
            return math.prod(nums)

        nums.sort()
        p = [num for num in nums if num > 0]
        n = [num for num in nums if num < 0]
        max_prod = float('-inf')
        if len(n) >=3:
            max_prod = max(max_prod, n[-1]*n[-2]*n[-3])
        if len(p) >=3:
            max_prod = max(max_prod, p[-1]*p[-2]*p[-3])
        if len(n)>=2 and len(p)>0:
            max_prod = max(max_prod, n[0]*n[1]*p[-1])
        if nums.count(0)>0:
            max_prod = max(max_prod, 0)
        return max_prod            