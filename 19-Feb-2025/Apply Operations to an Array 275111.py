# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)-1):
            if nums[i] ==  nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        counter = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[counter] = nums[i]
                counter += 1
            i +=1
    
        for j in range(counter, len(nums)):
            nums[j] = 0

        return nums