class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {} 
        self.heap = []  
        self.time = 0   

    def get(self, key: int) -> int:
        if key not in self.store: return -1
        self.time += 1
        value, _ = self.store[key]
        self.store[key] = (value, self.time)
        heapq.heappush(self.heap, (self.time, key))
        return value

    def put(self, key: int, value: int) -> None:
        self.time += 1
        self.store[key] = (value, self.time)
        heapq.heappush(self.heap, (self.time, key))

        if len(self.store) > self.capacity:
            while self.heap:
                old_time, old_key = heapq.heappop(self.heap)
                if self.store.get(old_key, (None, None))[1] == old_time:
                    del self.store[old_key]
                    break

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)