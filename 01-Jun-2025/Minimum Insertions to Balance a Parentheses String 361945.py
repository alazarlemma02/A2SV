# Problem: Minimum Insertions to Balance a Parentheses String - https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

class Solution:
    def minInsertions(self, s: str) -> int:
        required = 0
        st = []
        i, n = 0, len(s)
        
        while i < n:
            if s[i] == '(':
                st.append('(')
                i +=1
            else:
                if st:
                    st.pop()
                else:
                    required +=1

                if i < n-1 and s[i+1] == ')':
                    i +=2
                else:
                    required +=1
                    i +=1

        return required + len(st)*2

        