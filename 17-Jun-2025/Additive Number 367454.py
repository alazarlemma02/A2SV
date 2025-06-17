# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def dfs(n1, n2, rem):
            if (n1[0] == '0' and len(n1) >1) or (n2[0] == '0' and len(n2) >1):
                return False
            
            total = str(int(n1) + int(n2))
            m = len(total)
            if total == rem:
                return True

            if len(rem) <= len(n2): 
                return False    

            if total == rem[:m]:      
                n1 = n2
                n2 = rem[:m]
                rem = rem[m:]
                return dfs(n1, n2, rem)   

            return False     

        for i in range(1,n):
            for j in range(i):
                n1 = num[:j+1]
                n2 = num[j+1:i+1]
                rem = num[i+1:]
                if dfs(n1, n2, rem):
                    return True

        return False