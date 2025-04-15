# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_num = max(nums)
        nums_map = Counter(nums)

        for i in range(1, max_num+1):
            if i not in nums_map:
                return i
        return max_num + 1 if max_num > 0 else 1