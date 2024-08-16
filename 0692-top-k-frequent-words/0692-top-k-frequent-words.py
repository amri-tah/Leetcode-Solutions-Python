class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        
        max_heap = []
        for word, f in freq.items():
            heapq.heappush(max_heap, (-f, word))
        
        top_k_words = []
        for _ in range(k):
            f, freq_word = heapq.heappop(max_heap)
            top_k_words.append(freq_word)
        
        return top_k_words