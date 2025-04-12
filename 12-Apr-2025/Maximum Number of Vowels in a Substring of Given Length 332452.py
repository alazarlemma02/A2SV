# Problem: Maximum Number of Vowels in a Substring of Given Length - https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowel_set = {"a", "e", "i", "o", "u"}

        i, cnt, max_vowels = 0, 0, 0

        for j in range(n):
            if s[j] in vowel_set:
                cnt += 1
            
            if j - i + 1 == k:
                max_vowels = max(max_vowels, cnt)
                if s[i] in vowel_set:
                    cnt -= 1
                i +=1

        return max_vowels
            
        