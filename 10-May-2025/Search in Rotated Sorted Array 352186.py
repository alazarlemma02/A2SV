# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        def modifiedSearch(nums, target, left, right):
            if left > right: return -1

            mid = (right + left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if nums[left] <= target and target <= nums[mid]:
                    return modifiedSearch(nums, target, left, mid-1)
                else:
                    return modifiedSearch(nums, target, mid + 1, right)
            else:
                if nums[mid] <= target and target <= nums[right]:
                    return modifiedSearch(nums, target, mid + 1, right)
                else:
                    return modifiedSearch(nums, target, left, mid-1)

        return modifiedSearch(nums, target, left, right)