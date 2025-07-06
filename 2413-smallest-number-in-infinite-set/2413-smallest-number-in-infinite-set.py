class SmallestInfiniteSet:
    def __init__(self):
        self.i = 1
        self.heap = []
        self.set = set()

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.set.remove(smallest)
            return smallest
        else:
            smallest = self.i
            self.i += 1
            return smallest

    def addBack(self, num: int) -> None:
        if num < self.i and num not in self.set:
            heapq.heappush(self.heap, num)
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)