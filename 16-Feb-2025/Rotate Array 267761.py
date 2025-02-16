# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums.reverse()
        #This function is used to exchanges places of numbers in the array
        def exchange(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
            return nums
        exchange(nums, 0, k-1)
        exchange(nums, k, len(nums)-1)

            
        