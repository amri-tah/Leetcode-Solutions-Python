class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def dfs(open, close, path):
            if open == close == n:
                self.res.append("".join(path))
                return
            if open < n: dfs(open + 1, close, path + ["("])
            if close < open: dfs(open, close + 1, path + [")"])

        dfs(0, 0, [])
        return self.res