# Problem: Extra Characters in a String - https://leetcode.com/problems/extra-characters-in-a-string/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_end = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        root = trie.root

        memo = { len(s): 0 }
        def dfs(i):
            if i in memo:
                return memo[i]
            res = 1 + dfs(i+1)
            curr = root

            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.is_end:
                    res = min(res, dfs(j+1))
            memo[i] = res
            return res
            
        return dfs(0)
        