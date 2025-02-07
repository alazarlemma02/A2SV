# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives, negatives = [], []
        for num in nums:
            if  num > 0:
                positives.append(num)
            else:
                negatives.append(num)

        pos, neg = 0, 0
        for num in range(len(nums)):
            if num % 2 == 0:
                nums[num] = positives[pos]
                pos +=1
            else:
                nums[num] = negatives[neg]
                neg+=1
        return nums