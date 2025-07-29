class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 26: return chr(ord('A') + columnNumber - 1)
        n = (columnNumber - 1) // 26
        i = (columnNumber - 1) % 26
        return self.convertToTitle(n) + chr(ord('A') + i)