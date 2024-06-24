class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = Counter(words)
        return sorted(dict, key=lambda x:(-dict[x], x))[:k]