# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st, res = [], []

        def track(op, cl):
            if op == cl == n:
                res.append("".join(st))
                return

            if op < n:
                st.append("(")
                track(op+1, cl)
                st.pop()

            if cl < op:
                st.append(")")
                track(op, cl+1)
                st.pop()

        track(0, 0)
        return res