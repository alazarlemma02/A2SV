# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = set(nums)
        print(numbers)
        print(nums)
        if len(nums) - len(numbers) != 0:
            return True
        else:
            return False