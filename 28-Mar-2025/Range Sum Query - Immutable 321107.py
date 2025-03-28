# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        pref_sum = 0
        for i in range(left, right +1):
            pref_sum += self.nums[i]
        return pref_sum
        