class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        x1, y1 = list(coordinate1)
        x2, y2 = list(coordinate2)
        x1, x2, y1, y2 = ord(x1)-ord("a"), ord(x2)-ord("a"), int(y1), int(y2)
        color1 = (x1 + y1) % 2
        color2 = (x2 + y2) % 2
        return color1==color2