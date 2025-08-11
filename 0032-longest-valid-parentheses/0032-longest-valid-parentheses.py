class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxlen = 0
        for i, par in enumerate(s):
            if par=="(": stack.append(i)
            else:
                stack.pop()
                if not stack: stack.append(i)
                else: maxlen = max(maxlen, i-stack[-1])
        return maxlen