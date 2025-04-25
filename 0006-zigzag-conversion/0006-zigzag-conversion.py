class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1: return s
        d, i = 1, 0
        output = ["" for i in range(numRows)]
        for letter in s:
            if i==0: d=1
            if i==numRows-1: d=-1
            output[i]+=letter
            i+=d
        return "".join(output)