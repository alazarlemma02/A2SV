# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:
    prefix_sum = []
    def __init__(self, nums: List[int]):
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        self.prefix_sum = nums
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0: return self.prefix_sum[right]
        res = self.prefix_sum[right] - self.prefix_sum[left-1]
        return res
        