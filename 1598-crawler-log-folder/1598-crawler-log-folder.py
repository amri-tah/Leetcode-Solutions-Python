class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for operation in logs:
            if operation == "./":
                continue
            elif operation == "../":
                if len(stack)>0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(operation)
            print(stack)
        return len(stack)