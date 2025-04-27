# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        res = [0] * n

        for i in range(n):

            while st and temperatures[st[-1]] < temperatures[i]:
                dis = i - st[-1]
                res[st[-1]] = dis
                st.pop()

            st.append(i)
        return res        