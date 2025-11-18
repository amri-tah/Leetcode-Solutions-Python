class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        res = []
        top = 0
        for i in range(1, n+1):
            if stack==target: return res
            if target[top]!=i:
                res.extend(["Push","Pop"])
            else: 
                stack.append(i)
                res.append("Push")
                top+=1
        return res
