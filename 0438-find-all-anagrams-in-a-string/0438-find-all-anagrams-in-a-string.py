class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s) : return []
        
        scount, pcount = {}, {}
        left = 0
        
        for i in range(len(p)):
            scount[s[i]] = 1+scount.get(s[i], 0)
            pcount[p[i]] = 1+pcount.get(p[i], 0)
        
        if scount == pcount: res = [0]
        else: res = []
        
        for right in range(len(p), len(s)):
            scount[s[right]] = 1 + scount.get(s[right], 0)
            scount[s[left]] -= 1
            
            if scount[s[left]] == 0: scount.pop(s[left])
            left+=1
            if scount == pcount: res.append(left)
        return res
            
            