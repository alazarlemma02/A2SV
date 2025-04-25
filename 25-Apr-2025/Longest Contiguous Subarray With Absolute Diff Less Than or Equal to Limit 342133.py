# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        minQ, maxQ = deque(), deque()

        i, max_arr = 0, 0

        for j in range(n):
            while maxQ and nums[j] > maxQ[-1]:
                maxQ.pop()
            maxQ.append(nums[j])
            while minQ and nums[j] < minQ[-1]:
                minQ.pop()
            minQ.append(nums[j])


            while maxQ[0] - minQ[0] > limit:
                if maxQ[0] == nums[i]:
                    maxQ.popleft()
                if minQ[0] == nums[i]:
                    minQ.popleft()
                i +=1
            max_arr = max(max_arr, j - i + 1)

        return max_arr
        