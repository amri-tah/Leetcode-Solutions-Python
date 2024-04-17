class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t): return False
        
        shash, thash, stable = {}, {}, []
        i = 0
        for s_char in s:
            if s_char in shash: stable.append(shash[s_char])
            else:
                shash[s_char] = i
                stable.append(i)
                i+=1

        i = 0
        for j, t_char in enumerate(t):
            if t_char not in thash:
                thash[t_char] = i
                i+=1
            if thash[t_char]!=stable[j]: return False
        
        return True