class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        output = ""
        for i in range(len(s)):
            # odd len
            left, right = i, i
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            if right-left-1>maxLen: 
                maxLen = right-left-1
                output = s[left+1:right]
            
            # even len
            left, right = i, i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            if right-left-1>maxLen: 
                maxLen = right-left-1
                output = s[left+1:right]
        return output
