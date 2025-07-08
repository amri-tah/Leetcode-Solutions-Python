class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(start, path, pathsum):
            if len(path) == k and pathsum == n:
                res.append(path[:])
                return
            if len(path) > k or pathsum > n: return
            for num in range(start, 10):
                path.append(num)
                dfs(num + 1, path, pathsum + num)
                path.pop()

        dfs(1, [], 0)
        return res