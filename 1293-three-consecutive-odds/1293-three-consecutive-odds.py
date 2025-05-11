class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        curr = 0
        for num in arr:
            if num%2!=0: 
                curr+=1
                if curr==3: return True
            else: curr=0
        return False
        