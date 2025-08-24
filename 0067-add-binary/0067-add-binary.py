class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b=int(a, 2), int(b, 2)
        while b!=0:
            carry = a&b
            a=a^b
            b=carry<<1
        return bin(a)[2:]