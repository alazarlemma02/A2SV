# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

from collections import Counter

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, char_idx, word):
        prev_idx = -1
        for c in word:
            if c not in char_idx:
                return False

            idx_list = char_idx[c]
            pos = bisect.bisect_right(idx_list, prev_idx)
            if pos == len(idx_list):
                return False
            prev_idx = idx_list[pos]
        return True

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        trie = Trie()
        trie.insert(s)

        char_idx = defaultdict(list)
        for i, c in enumerate(s):
            char_idx[c].append(i)

        for word in words:
            if trie.search(char_idx, word):
                res += 1
        return res

