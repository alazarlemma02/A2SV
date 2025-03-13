# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0: return 1
        if n == 1:
            return 0 if nums[0]==val else 1
        left, right = 0, 0

        while right < n:
            if nums[right] != val:
                nums[left] = nums[right]
                left +=1
                
            right +=1
        return left


        
            