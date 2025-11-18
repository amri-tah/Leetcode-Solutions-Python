class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxarea = max(maxarea, height * (i - idx))
                start = idx
            stack.append((start, h))
        n = len(heights)
        for idx, height in stack:
            maxarea = max(maxarea, height * (n - idx))
        return maxarea