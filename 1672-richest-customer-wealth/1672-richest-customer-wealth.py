class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 1
        for i in range(len(accounts)):
            s=sum(accounts[i])
            if s>max:
                max=s
        return max