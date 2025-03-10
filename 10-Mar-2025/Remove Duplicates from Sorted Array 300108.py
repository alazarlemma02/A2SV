# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        left = right = 0
        while right < len(nums):
            curr = nums[right]
            while right < len(nums)-1 and nums[right+1]==curr:
                right +=1
            nums[left] = curr
            left +=1
            right +=1 
        return left
        
        