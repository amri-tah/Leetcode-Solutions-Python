class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        hash = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        queue = deque([""])
        for digit in digits:
            for _ in range(len(queue)):
                comb = queue.popleft()
                for letter in hash[digit]:
                    queue.append(comb+letter)
        return list(queue)