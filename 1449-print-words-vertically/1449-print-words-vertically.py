class Solution:
    def printVertically(self, s: str) -> List[str]:
        res = []
        s = s.split()
        maxlen = max(len(word) for word in s)
        for i in range(maxlen):
            temp = ""
            for strs in s:
                if i<len(strs):temp+=strs[i]
                else: temp+=" "
            temp = temp.rstrip() 
            res.append(temp)
        return res