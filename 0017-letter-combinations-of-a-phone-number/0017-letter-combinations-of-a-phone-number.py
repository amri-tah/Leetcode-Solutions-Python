class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        result = []
        hashmap = {
            2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
        }
        
        def backtrack(i, curr):
            if len(curr)==len(digits):
                result.append(curr)
                return
            
            for c in hashmap[int(digits[i])]:
                backtrack(i+1, curr+c)

        backtrack(0, "")
        return result