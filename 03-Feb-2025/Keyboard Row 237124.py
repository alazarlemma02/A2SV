# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution(object):
    def findWords(self, words):
        keyboard_list = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        output = []
        # bruteforce soln
        for word in words:
            counter = 0
            for key in keyboard_list:
                for char in word.lower():
                    if char in key:
                        counter += 1
                    else:
                        break
            if counter == len(word):
                output.append(word)
            counter = 0
        return output




        