class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        length = 0
        right = len(s)-1
        while s[right]!=" " and right>=0:
            right -= 1
            length += 1
        return length
            