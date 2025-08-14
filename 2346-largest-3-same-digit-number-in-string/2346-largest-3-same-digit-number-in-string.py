class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        maxsofar = 0
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                if int(num[i])>=maxsofar:
                    maxsofar=int(num[i])
                    res=num[i:i+3]
        return res