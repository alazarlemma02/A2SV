# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        vowel_set = {"a","e","i","o","u"}
        vowel_sub = 0

        for i in range(n):
            cnt_map = defaultdict(int)
            for j in range(i, n):
                if word[j] in vowel_set:
                    cnt_map[word[j]] +=1
                else:
                    break
                
                if len(cnt_map) >= len(vowel_set):
                    vowel_sub +=1

        return vowel_sub

