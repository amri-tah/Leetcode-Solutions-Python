class Solution:
    def makeFancyString(self, s: str) -> str:
        output = s[0]
        for i in range(1, len(s)-1):
            if s[i]==s[i-1] and s[i]==s[i+1]: continue
            else: output+=s[i]
        output+=s[-1] if len(s)>1 else ""
        return output