# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        counter = 1
        for num in range(len(nums)-1):
            if nums[num] <= nums[num+1]:
                continue
            if counter < 1:
                return False
            if num == 0 or nums[num+1] >= nums[num-1]:
                nums[num] = nums[num+1]
            else:
                nums[num+1] = nums[num]
            counter -=1
        return True

        
        