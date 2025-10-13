# Problem: Maximum Number of Operations With the Same Score II - https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        memo = [[-1] * n for _ in range(n)]

        def dp(left: int, right: int, target_sum: int) -> int:
            if left >= right:
                return 0
            if memo[left][right] != -1:
                return memo[left][right]

            res = 0

            if nums[left] + nums[left + 1] == target_sum:
                res = max(res, 1 + dp(left + 2, right, target_sum))

            if nums[right - 1] + nums[right] == target_sum:
                res = max(res, 1 + dp(left, right - 2, target_sum))

            if nums[left] + nums[right] == target_sum:
                res = max(res, 1 + dp(left + 1, right - 1, target_sum))

            memo[left][right] = res
            return res

        ans = 0
        ans = max(ans, 1 + dp(2, n - 1, nums[0] + nums[1]))
        ans = max(ans, 1 + dp(0, n - 3, nums[-2] + nums[-1]))
        ans = max(ans, 1 + dp(1, n - 2, nums[0] + nums[-1]))

        return ans
