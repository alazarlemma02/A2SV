# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = Counter(nums)
        return [num for num in nums if nums[num] > n//3]
        