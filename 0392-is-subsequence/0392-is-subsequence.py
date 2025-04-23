class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t): return False
        if not s: return True
        p1 = p2 = 0
        while p1<len(s) and p2<len(t):
            if s[p1]==t[p2]: p1+=1
            p2+=1
        return p1==len(s)