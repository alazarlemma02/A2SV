# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        opps = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in opps:
                st.append(int(token))
            else:
                l = st[-1]
                st.pop()
                r = st[-1]
                st.pop()
                if token == '+':
                    st.append(l + r)
                elif token == '-':
                    st.append(r - l)
                elif token == '*':
                    st.append(l * r)
                else:
                    st.append(int(r / l))

        return st[-1]

