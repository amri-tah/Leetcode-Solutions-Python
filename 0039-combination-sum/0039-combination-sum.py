class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(start, pathsum, path):
            if pathsum > target: return
            if pathsum == target:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, pathsum + candidates[i], path)
                path.pop()

        dfs(0, 0, [])
        return result