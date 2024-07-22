class Solution:
    def fib(self, n: int) -> int:
        if n==0: return 0
        x, y = 0, 1
        for i in range(2, n+1):
            temp = x+y
            x = y
            y = temp
        return y