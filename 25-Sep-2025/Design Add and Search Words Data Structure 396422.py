# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:

        def helper(node: TrieNode, idx: int):
            if idx == len(word):
                return node.is_end
            if word[idx] == ".":
                for child in node.children.values():
                    if helper(child, idx+1):
                        return True
                return False
            if word[idx] not in node.children:
                return False
            return helper(node.children[word[idx]], idx+1)

        return helper(self.root, 0)        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)