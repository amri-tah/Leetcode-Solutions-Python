class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = -1
        output = ["0"]*len(s)
        for bit in s:
            if bit=="1": count+=1
        output[-1]="1"
        
        if count >=1:
            # make 0-> count-1 values "1"
            for index in range(count):
                output[index]="1"
        return "".join(output)
                