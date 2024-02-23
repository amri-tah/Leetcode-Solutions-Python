class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))

    def pop(self) -> int:
        if not self.empty():
            return self.queue.pop(0)

    def top(self) -> int:
        if not self.empty():
            return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()