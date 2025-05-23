# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        st = []
        min_holder = []
        cur_min = nums[0]
        
        for i in range(1, n):
            while st and nums[i] >= st[-1]:
                st.pop()
                min_holder.pop()

            if st and nums[i] > min_holder[-1]:
                return True

            st.append(nums[i])
            min_holder.append(cur_min)
            cur_min = min(cur_min, nums[i])

        return False