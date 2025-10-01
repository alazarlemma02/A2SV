# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

            if len(curr.suggestions) < 3:
                curr.suggestions.append(word)
                curr.suggestions.sort()
            else:
                if word < curr.suggestions[-1]:
                    curr.suggestions[-1] = word
                    curr.suggestions.sort()

    def search(self, prefix: str):
        curr = self.root
        for p in prefix:
            if p not in curr.children:
                return None
            curr = curr.children[p]
        return curr

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        trie = Trie()
        for p in products:
            trie.insert(p)

        res = []
        prefix = ""
        for c in searchWord:
            prefix += c
            node = trie.search(prefix)
            if not node:
                res.append([])
            else:
                res.append(node.suggestions)
        return res