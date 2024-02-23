class Solution:
    def makeGood(self, s: str) -> str:
        goodstring = []
        for char in s:
            if goodstring and abs(ord(char) - ord(goodstring[-1])) == 32:
                goodstring.pop()
            else:
                goodstring.append(char)
                
        return "".join(goodstring)
            