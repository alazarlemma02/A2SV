# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution(object):
    def romanToInt(self, s):
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        for i in range(len(s)):
            left = roman[s[i]]
            if(i+1 < len(s)):
                right = roman[s[i+1]]
                if(left >= right):
                    result+=left
                else:
                    result-=left
            else:
               result+=left
        return result  
        