# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class Trie():
    def __init__(self):
        self.children = defaultdict(int)
        self.val = 0

    def insert(self, word: str, new_val: int) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
            curr.val += new_val

    def search(self, prefix: str) -> int:
        curr = self
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.val

class MapSum:
    def __init__(self):
        self.key_val_map = defaultdict(int)
        self.tr = Trie()

    def insert(self, key: str, val: int) -> None:
        new_val = val - self.key_val_map[key]
        self.key_val_map[key] = val
        self.tr.insert(key, new_val)

    def sum(self, prefix: str) -> int:
        return self.tr.search(prefix)
 
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)