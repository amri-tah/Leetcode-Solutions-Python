class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        seen = []
        
        while (n!=1) and (n not in seen):
            temp=0
            seen.append(n)
            n = list(str(n))
            for x in n:
                temp += int(x)**2
            n = temp
            if temp == 1:
                return True
        return False