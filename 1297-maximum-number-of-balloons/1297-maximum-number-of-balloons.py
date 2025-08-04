class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        freq = defaultdict(int)
        for char in text:
            if char in target: freq[char]+=1
        freq['l'] //= 2
        freq['o'] //= 2
        count = float('inf')
        for char in "balon":
            count = min(count, freq[char])
        return count