# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        st = []

        for char in s:
            if char == "*" and len(st) > 0:
                st.pop()
            else:
                st.append(char)

        return "".join(st)

        