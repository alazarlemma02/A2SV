# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        s = s.lower()
        s = s.split("@")
        char_set = {'+', '-', '(', ')', ' '} 
        if len(s) > 1:
            email = f"{s[0][0]}*****{s[0][-1]}@{s[-1]}"
            return email
        number = []
        for num in range(len(s[0])):
            if s[0][num] not in char_set:
                number.append(s[0][num])
        phone_number = "".join(number)
        n = len(phone_number)
        if n == 10:
            return f"***-***-{phone_number[-4:]}"
        if n == 11:
            return f"+*-***-***-{phone_number[-4:]}"
        if n == 12:
            return f"+**-***-***-{phone_number[-4:]}"
        if n == 13:
            return f"+***-***-***-{phone_number[-4:]}"