class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        while self.curr!=len(self.stack)-1: self.stack.pop()
        self.stack.append(url)
        self.curr=len(self.stack)-1
        return None

    def back(self, steps: int) -> str:
        self.curr = max(self.curr-steps, 0)
        return self.stack[self.curr]
        
    def forward(self, steps: int) -> str:
        self.curr = min(self.curr+steps, len(self.stack)-1)
        return self.stack[self.curr]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)