class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[':']'}
        stack = []
        for letter in s:
            if letter in brackets: stack.append(letter)
            elif stack:
                popped = stack.pop()
                if letter!=brackets[popped]: return False
            else: return False
        if stack: return False
        return True