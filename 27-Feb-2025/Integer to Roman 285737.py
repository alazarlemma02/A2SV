# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_hash = {
            1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
            90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"
        }
        divs = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ""
        curr = len(divs)-1

        while curr >= 0:
            if divs[curr] <= num:
                res = num // divs[curr]
                roman += roman_hash[divs[curr]] * res
                num %= divs[curr]
            curr -= 1
        return roman
        
        

        