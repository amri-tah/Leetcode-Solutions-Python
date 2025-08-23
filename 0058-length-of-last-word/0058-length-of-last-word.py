class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        i=len(s)-1
        while s[i]!=" " and i>=0:
            i-=1
        return len(s)-i-1