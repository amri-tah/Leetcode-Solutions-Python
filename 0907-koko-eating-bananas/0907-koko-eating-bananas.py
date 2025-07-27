class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        output = right
        while left<=right:
            k = (left+right)//2
            hours = 0
            for pile in piles:
                hours+=math.ceil(pile/k)
            if hours<=h:
                output = min(output, k)
                right = k-1
            else:
                left = k+1
        return output