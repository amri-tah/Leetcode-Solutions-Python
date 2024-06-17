class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[':']'}
        stack = []
        for letter in s:
            if letter in brackets: stack.append(letter)
            else:
                if stack:
                    popped = stack.pop()
                    if letter!=brackets[popped]: return False
                else: return False
                
        return len(stack)==0