class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if s==s[::-1]: return s
        
        # def pallindrome(s):
        #     return s==s[::-1]
        
        # # Brute Force Approach: using 2 pointer for indices and checking if pallindrome
        # maxP = s[0]
        # for left in range(len(s)):
        #     for right in range(left+1, len(s)):
        #         if pallindrome(s[left:right+1]) and right-left+1>len(maxP): 
        #             maxP = s[left:right+1]
                    
        # return maxP

        # DP Approach: consider every character as center and expand outwards
        result = ""
        max_len = 0

        for i in range(len(s)):
            # Odd Length
            l, r = i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>max_len:
                    result = s[l:r+1]
                    max_len = r-l+1
                l-=1
                r+=1
                
            # Even Length
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>max_len:
                    result = s[l:r+1]
                    max_len = r-l+1
                l-=1
                r+=1
        return result