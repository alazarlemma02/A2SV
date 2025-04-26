# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        score = 0

        for par in s:
            if par == "(":
                st.append(score)
                score = 0
            else:
                score = st[-1] + max(2*score, 1)
                st.pop()

        return score
        