# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        res = nums[0]
        for num in nums[1:]:
            res ^= num
        
        idx = 0
        while res & 1 == 0:
            idx +=1
            res >>=1
        
        left, right = [], []
        for num in nums:
            curr = num >> idx
            if left and curr & 1 == 0:
                left[-1] = left[-1] ^ num
            elif right and curr & 1 == 1:
                right[-1] = right[-1] ^ num
            elif curr & 1 == 0:
                left.append(num)
            else:
                right.append(num)

        return left + right
        