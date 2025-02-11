# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        idx_map = defaultdict(int)
        for i in range(len(nums)):
            idx_map[nums[i]] = i
        
        for op in operations:
            idx = idx_map[op[0]]
            nums[idx] = op[1]
            idx_map[op[1]] = idx
            del idx_map[op[0]]
        
        return nums