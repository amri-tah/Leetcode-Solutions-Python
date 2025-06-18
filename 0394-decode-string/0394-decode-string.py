class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        output = ""
        for char in s:
            if char!="]": stack.append(char)
            else:
                substr = ""
                while stack and stack[-1]!="[":
                    substr=stack.pop()+substr
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                stack.append(substr*int(num))
        return "".join(stack)
