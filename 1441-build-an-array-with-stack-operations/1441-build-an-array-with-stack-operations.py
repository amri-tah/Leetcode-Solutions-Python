class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        stack = []
        j=0
        for number in range(1, n+1):
            if stack != target:
                result.append("Push")
                stack.append(number)
                if number == target[j]:
                    j+=1
                else:
                    result.append("Pop")
                    stack.pop()
        return result
        
            
            
            