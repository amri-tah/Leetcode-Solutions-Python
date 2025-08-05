class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        alloted = 0
        n = len(fruits)
        for fruit in fruits:
            for j in range(n):
                if fruit<=baskets[j]:
                    baskets[j]=0
                    alloted+=1
                    break
        return n-alloted