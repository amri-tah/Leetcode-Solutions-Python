class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        n = len(self.stack)
        self.stack.append(x)
        for i in range(n):
            popped = self.stack.popleft()
            self.stack.append(popped)

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()