class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        # Iterate thru each char in the string and push if not a closing bracket:
        for char in s:
            if char!="]": stack.append(char)
            else:
                # Pop out characters in between brackets
                substr = ""
                while stack[-1]!="[":
                    substr = stack.pop() + substr
                
                stack.pop() # Pop out opening bracket
                
                # Pop out digits
                subnumber = ""
                while stack and stack[-1].isdigit():
                    subnumber = stack.pop() + subnumber
                
                subnumber = int(subnumber)
                
                # Push the decoded substring
                stack.append(subnumber*substr)
        
        return "".join(stack)