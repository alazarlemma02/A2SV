# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = Counter(nums)
        return [num for num in nums if nums[num] > n//3]
        