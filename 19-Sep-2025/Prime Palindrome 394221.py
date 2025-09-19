# Problem: Prime Palindrome - https://leetcode.com/problems/prime-palindrome/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(num):
            if num < 2:
                return False
            if num in (2, 3):
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(num))+1, 2):
                if num % i == 0:
                    return False
            return True
        if n <= 2:
            return 2
        if n <= 11:
            for p in [2, 3, 5, 7, 11]:
                if p >= n:
                    return p
        
        length = len(str(n))
        while True:
            half_len = (length + 1) // 2
            start = 10 ** (half_len - 1)
            end = 10 ** half_len
            for half in range(start, end):
                s = str(half)
                pd = int(s + s[-2::-1])
                
                if pd >= n and is_prime(pd):
                    return pd
            length += 1
