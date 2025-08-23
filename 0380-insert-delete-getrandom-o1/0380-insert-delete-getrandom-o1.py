class RandomizedSet:
    def __init__(self):
        self.values = []
        self.values_i = {} # val: i

    def insert(self, val: int) -> bool:
        if val in self.values_i: return False
        self.values_i[val]=len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values_i: return False
        # swap to end
        ind = self.values_i[val]
        self.values_i[self.values[-1]] = ind
        self.values[-1], self.values[ind] = self.values[ind], self.values[-1]
        self.values.pop()
        del self.values_i[val]
        return True

    def getRandom(self) -> int:
        ind = random.randint(0, len(self.values)-1)
        return self.values[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()