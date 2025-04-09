# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        avgs = []

        prx_sum = 0
        for i in range(n):
            nums[i] += prx_sum
            prx_sum = nums[i]

        for j in range(n):
            if j-k >=0 and j+k < n:
                cur = nums[j-k-1] if j-k > 0 else 0

                res = (nums[j+k] - cur) // ((j+k)-(j-k) + 1)
                avgs.append(res)
            else:
                avgs.append(-1)

        return avgs