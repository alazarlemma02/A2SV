# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def check(part):
            if len(part) > 1 and part[0] == '0': return False
            if not 0 <= int(part) < 256: return False
            return True

        def backtrack(idx, curr):
            if len(curr) == 4 and idx == n:
                res.append(".".join(curr))
                return
            if len(curr) > 4:
                return
            
            for j in range(idx, min(idx+3, n)):
                part = s[idx:j+1]
                if check(part):
                    curr.append(part)
                    backtrack(j+1, curr)
                    curr.pop()
            
        backtrack(0, [])
        return res