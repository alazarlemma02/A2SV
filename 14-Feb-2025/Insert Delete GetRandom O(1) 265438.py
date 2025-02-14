# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.values = []
        self.value_to_idx = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.value_to_idx:
            self.value_to_idx[val] = len(self.values)
            self.values.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.value_to_idx:
            val_idx_to_remove = self.value_to_idx[val]
            last_value = self.values[-1]
            self.values[val_idx_to_remove] = last_value
            self.value_to_idx[last_value] = val_idx_to_remove

            self.values.pop()
            del self.value_to_idx[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()