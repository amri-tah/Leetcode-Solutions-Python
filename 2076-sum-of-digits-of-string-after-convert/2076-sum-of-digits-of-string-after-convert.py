class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join(str(ord(ch) - ord('a') + 1) for ch in s)
        for _ in range(k):
            s = str(sum(int(digit) for digit in s))
        return int(s)