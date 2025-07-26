class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for token in tokens:
            if token.lstrip('-').isdigit(): stack.append(int(token))
            else:
                first = stack.pop()
                second = stack.pop()
                if token == '+': stack.append(first+second)
                elif token == '-': stack.append(second-first)
                elif token == '*': stack.append(first*second)
                elif token == '/': stack.append(int(second/first))
        return stack[0]
