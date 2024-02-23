class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        temp = {"(": ")", "{": "}", "[":"]"}
        for letter in s:
            if letter in temp:
                stack.append(letter)
            elif letter in [")", "}", "]"]:
                if len(stack)==0:
                    return False
                elif letter==temp[stack.pop()]:
                    continue
                else:
                    return False
            
        return len(stack)==0
            