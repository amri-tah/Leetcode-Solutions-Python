class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            # isolate each bit at a time
            abit = a & 1
            bbit = b & 1
            cbit = c & 1

            # if c==1 then need a and or b to be 1
            if cbit:
                if not (abit|bbit): flips+=1
            # if c==0 then need to flip both a and b if they 1
            elif not cbit:
                if abit: flips+=1
                if bbit: flips+=1
            a>>=1
            b>>=1
            c>>=1
        return flips