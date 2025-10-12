class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        for sch in s:
            if sch in hash: hash[sch]+=1
            else: hash[sch]=1
        for tch in t:
            if tch not in hash: return False
            else: hash[tch]-=1
            if hash[tch]==0: del hash[tch]
        return False if hash else True