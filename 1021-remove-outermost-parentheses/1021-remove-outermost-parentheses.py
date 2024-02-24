class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        open, close = 0, 0
        start = 0
        for index in range(len(s)):
            if s[index]=="(":
                open+=1
            else:
                close+=1
                
            if open==close:
                result+= s[start+1:index]
                start=index+1
                open, close = 0,0
                
        return result
            