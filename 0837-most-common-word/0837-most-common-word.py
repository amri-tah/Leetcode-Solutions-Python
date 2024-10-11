class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para = re.split(r'\W+', paragraph.lower())
        banned = set(banned)
        count = Counter(para)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        while heap:
            freq, word = heapq.heappop(heap)
            if word not in banned and word: return word
