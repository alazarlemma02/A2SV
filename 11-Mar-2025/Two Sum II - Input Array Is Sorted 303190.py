# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        res = []
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                res = [left+1, right+1]
                return res
            if total < target:
                left +=1
            else:
                right -=1
