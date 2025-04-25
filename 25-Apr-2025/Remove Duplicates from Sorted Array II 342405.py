# Problem: Remove Duplicates from Sorted Array II - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution(object):
    def removeDuplicates(self, nums):
        left = right = 0
        while right < len(nums):
            curr = nums[right]
            count = 1
            while right < len(nums)-1 and nums[right+1]==curr:
                right +=1
                count +=1
            nums[left] = curr
            left +=1
            if count > 1:
                nums[left] = curr
                left +=1
            right +=1
        return left
        