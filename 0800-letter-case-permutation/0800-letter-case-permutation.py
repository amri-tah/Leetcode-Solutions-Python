class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # if letter is alphabet then -> lowercase
        #                            -> uppercase

        # if number: continue

        res = []

        def backtrack(index: int, path: str):
            if index == len(s):
                res.append(path)
                return

            if s[index].isalpha():
                backtrack(index + 1, path + s[index].lower())
                backtrack(index + 1, path + s[index].upper())
            else:
                backtrack(index + 1, path + s[index])

        backtrack(0, "")
        return res