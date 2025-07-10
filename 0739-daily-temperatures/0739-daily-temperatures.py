class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i-j
            stack.append(i)
        return result