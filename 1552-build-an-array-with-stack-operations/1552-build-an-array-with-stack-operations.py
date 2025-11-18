class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        res = []
        top = 0
        for i in range(1, n+1):
            if stack==target: return res
            stack.append(i)
            res.append("Push")
            if target[top]!=stack[-1]:
                stack.pop()
                res.append("Pop")
            else: top+=1
        return res
