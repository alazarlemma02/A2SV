# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        st = []
        s_cnt = Counter(s)
        visted = defaultdict(bool)

        for char in s:
            s_cnt[char] -=1
            if visted[char]:
                continue

            while st and st[-1] > char and s_cnt[st[-1]] > 0:
                visted[st[-1]] = False
                st.pop()
                
            st.append(char)
            visted[char] = True
               
        return "".join(st)