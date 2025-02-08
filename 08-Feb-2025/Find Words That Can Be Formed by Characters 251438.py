# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        chars_map = {}
        for char in chars:
            if char in chars_map:
                chars_map[char] +=1
            else:
                chars_map[char] = 1
        for word in words:
            temp = chars_map.copy()
            c = 0
            for char in range(len(word)):
                if word[char] in temp and temp[word[char]]>0:
                    c+=1
                    temp[word[char]] -= 1
            if c == len(word):
                count += c
        return count
