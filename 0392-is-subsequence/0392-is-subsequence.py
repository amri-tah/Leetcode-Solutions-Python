class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t): return False
        if not s: return True
        p = 0
        for letter in t:
            if p==len(s): return True
            if letter==s[p]: p+=1
        return p==len(s)