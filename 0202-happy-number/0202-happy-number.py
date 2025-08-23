class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            temp = 0
            while n > 0:
                temp += (n % 10) ** 2
                n //= 10
            n = temp
        return n == 1