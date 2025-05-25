# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        path = path.split("/")

        for p in path:
            if p == "" or p == "." or (not st and p == ".."):
                continue
            if st and p == "..":
                st.pop()
            else:
                st.append(p)

        st = "/" + "/".join(st)
        return st        