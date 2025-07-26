class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        y_count = defaultdict(int)
        for _, y in points:
            y_count[y] += 1

        result = total_pairs = 0
        for count in y_count.values():
            pairs = count * (count - 1) // 2  
            result = (result + total_pairs * pairs) % MOD
            total_pairs = (total_pairs + pairs) % MOD

        return result