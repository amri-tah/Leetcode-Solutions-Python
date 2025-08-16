class Solution:
    def maximum69Number (self, num: int) -> int:
        # change the leftmost 6 to 9 
        num = list(str(num))
        for i in range(len(num)):
            if num[i]=='6': 
                num[i]='9'
                break
        return int(''.join(num))
