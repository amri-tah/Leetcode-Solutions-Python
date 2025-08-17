class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(start, pathsum):
            if pathsum==amount: return 1 # there exists 1 path
            if pathsum>amount or start==len(coins): return 0
            if (start, pathsum) in cache: return cache[(start, pathsum)]
            # 2 choices, take start or skip start
            take = dfs(start, pathsum+coins[start])
            skip = dfs(start+1, pathsum)
            cache[(start, pathsum)]=take+skip
            return cache[(start, pathsum)]
        return dfs(0, 0)
