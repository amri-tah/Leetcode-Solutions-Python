class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = defaultdict(int)
        minelement = float('inf')
        for b1 in basket1:
            freq[b1]+=1
            minelement = min(minelement, b1)
        for b2 in basket2:
            freq[b2]-=1
            minelement = min(minelement, b2)

        transfer = []
        for val, bal in freq.items():
            if bal==0: continue # already balanced
            if bal%2!=0: return -1 # odd number of values
            transfer.extend([val] * abs(bal // 2))  # Add half the imbalance
        if not transfer: return 0

        transfer.sort()
        total = len(transfer) // 2
        cost = 0
        for i in range(total):
            cost += min(transfer[i], 2 * minelement)
        return cost