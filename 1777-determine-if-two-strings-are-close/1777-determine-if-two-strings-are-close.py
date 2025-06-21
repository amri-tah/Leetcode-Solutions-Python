class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        if (
            sorted(freq1.values()) != sorted(freq2.values())
            or freq1.keys() != freq2.keys()
        ):
            return False
        return True
