# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        i, max_ones, curr_cnt = 0, 0, 0
        zero_cnt = 0

        for j in range(n):
            if nums[j] == 0:
                zero_cnt +=1
            curr_cnt +=1

            while zero_cnt > k:
                if nums[i] == 0:
                    zero_cnt -=1
                i +=1
                curr_cnt -=1

            max_ones = max(max_ones, curr_cnt)
        return max_ones

        