class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = 0
        for i in range(len(s)):
            zeros, ones = 0, 0
            for j in range(i, len(s)):
                if s[j]=="1":ones+=1
                if s[j]=="0":zeros+=1
                if ones<=k or zeros<=k: count+=1
                else: break
        return count