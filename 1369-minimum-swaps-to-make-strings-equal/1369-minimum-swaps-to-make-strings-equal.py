class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0
        for ch1, ch2 in zip(s1, s2):
            if ch1=="x" and ch2=="y": xy+=1
            elif ch1=="y" and ch2=="x": yx+=1
        if (xy+yx)%2!=0: return -1
        res = xy//2 + yx//2
        if xy%2!=0: res+=2
        return res
