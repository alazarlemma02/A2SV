# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        
        """
        While current n is not prime
            we continue replacing with its prime factors

        how do we know n is_prime?
        how can we capture the prime factor of n

        Example:
            6 = 2 * 3
            1. 6 / 2 = 3 => if this ans is prime or not

        better to have a separate method to check prime
        def is_prime(num):
            ...
            return True/False

        rule:
            if curr num is_prime or n <= 5:
                return n
        
        4 = 2 * 2 => 2 + 2 = 4?
        """

        def is_prime(num):
            if num < 2:
                return False
            if num in (2, 3):
                return True
            if num % 2 == 0:
                return False
            div = 0
            for i in range(3, int(math.sqrt(num))+1, 2):
                if num % i == 0:
                    return False
            return True
        
        if n <= 5: return n
        rep = n
        while not is_prime(rep):
            cur_sum = 0
            curr = rep
            for i in range(2, int(math.sqrt(curr)) + 1):
                while curr % i == 0:
                    cur_sum += i
                    curr //= i
            if curr > 1:
                cur_sum += curr
            if cur_sum == 0:
                break
            rep = cur_sum
        return rep

        