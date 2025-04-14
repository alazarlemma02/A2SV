# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)

        nums.sort()
        min_diff, res = float('inf'), 0

        for i in range(n):
            left, right = i + 1, n-1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                diff = abs(curr - target)
                if diff < min_diff:
                    min_diff, res = diff, curr
                if curr < target:
                    left += 1
                else:
                    right -= 1
        return res


        