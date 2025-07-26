class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack: curr_min = min(val, self.stack[-1][1])
        else: curr_min=val
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()