# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        is_gcd = False
        small = nums[0]
        large = nums[-1]
        curr = small

        while curr > 1:
            if small % curr == 0 and large % curr == 0:
                return curr
            curr -= 1
        return curr
        