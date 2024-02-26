class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxL = 0
        visited = set()
        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left+=1
            visited.add(s[right])
            maxL = max(maxL, right-left+1)
        return maxL