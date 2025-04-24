# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for char in s:
            if char.isdigit() and len(st) > 0:
                st.pop()
            else:
                st.append(char)
        return "".join(st)
