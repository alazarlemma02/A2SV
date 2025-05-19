# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        no_st = []
        st = []
        curr = ""
        k = 0

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                no_st.append(k)
                st.append(curr)
                k = 0
                curr = ''
            elif char == ']':
                prev_str = st.pop()
                count = no_st.pop()
                curr = prev_str + curr * count
            else:
                curr += char

        return curr

        
        