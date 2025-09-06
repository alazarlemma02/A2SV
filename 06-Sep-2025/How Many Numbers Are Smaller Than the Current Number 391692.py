# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        nums_final = []
        for i in nums:
            count = 0
            for j in nums:
                if j!=i and j<i:
                    count +=1
            nums_final.append(count)
        return nums_final
        