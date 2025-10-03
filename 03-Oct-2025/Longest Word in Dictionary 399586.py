# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.roots = TrieNode()

    def insert(self, word):
        curr = self.roots

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word):
        curr = self.roots

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
            if not curr.is_end:
                return False
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        res = []
        for word in words:
            trie.insert(word)

        for word in words:
            if trie.search(word):
                res.append(word)
        if not res: return ""

        res.sort(reverse = True)
        print(res)
        ans = res[0]
        for w in res:
            if len(w) >= len(ans):
                ans = min(ans, w)
        return ans