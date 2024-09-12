class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        output = len(words)
        for word in words:
            word = set(word)
            for w in word:
                if w not in allowed:
                    output-=1
                    break
        return output