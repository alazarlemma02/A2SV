# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.roots = TreeNode()

    def insert(self, word):
        curr = self.roots
        for w in word:
            if w not in curr.children:
                curr.children[w] = TreeNode()
            curr = curr.children[w]
        curr.is_end = True

    def search(self, word):
        curr = self.roots
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.is_end

class Solution:
    def partitionString(self, s: str) -> List[str]:
        trie = Trie()
        res = []
        curr = ""

        for char in s:
            curr += char
            if not trie.search(curr):
                res.append(curr)
                trie.insert(curr)
                curr = ""
        return res

