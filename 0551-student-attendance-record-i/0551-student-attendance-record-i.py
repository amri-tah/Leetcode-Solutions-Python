class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = late = 0
        for i in range(len(s)):
            if s[i]=="L": 
                late+=1
            else:
                if s[i]=="A":
                    absent+=1
                late = 0
                
            if absent==2 or late==3: return False
        return True
        