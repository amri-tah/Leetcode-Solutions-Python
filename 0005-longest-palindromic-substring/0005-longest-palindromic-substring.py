class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]: return s
        
        def pallindrome(s):
            return s==s[::-1]
        
        # Brute Force Approach: using 2 pointer for indices and checking if pallindrome
        maxP = s[0]
        for left in range(len(s)):
            for right in range(left+1, len(s)):
                if pallindrome(s[left:right+1]) and right-left+1>len(maxP): maxP = s[left:right+1]
                    
        return maxP