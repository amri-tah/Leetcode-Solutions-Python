class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        n = len(potions)
        for spell in spells:
            left, right = 0, n-1
            target = (success + spell - 1) // spell
            while left<=right:
                mid = (left+right)//2
                if potions[mid]>=target: right=mid-1
                else: left=mid+1
            res.append(n-left)
        return res