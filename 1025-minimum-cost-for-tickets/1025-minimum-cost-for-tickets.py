class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}
        def dfs(start):
            if start==len(days): return 0
            if start in cache: return cache[start]
            cache[start] = float('inf')
            # 3 choices -> 1 day, 7 days or 30 days
            for day, cost in zip([1, 7, 30], costs):
                j = start
                while j<len(days) and days[j]<days[start]+day:
                    j+=1
                cache[start] = min(cache[start], cost+dfs(j))
            return cache[start]
        return dfs(0)