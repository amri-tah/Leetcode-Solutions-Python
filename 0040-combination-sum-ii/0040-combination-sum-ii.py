class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        def backtrack(i, currsum, path):
            if currsum==target: 
                self.res.append(path[:])
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]: continue
                if currsum + candidates[j] > target: break
                backtrack(j+1, currsum+candidates[j], path+[candidates[j]])
        backtrack(0, 0, [])
        return self.res