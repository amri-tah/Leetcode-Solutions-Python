class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = [0]*26

        for letter in s:
            count[ord(letter)-ord("a")] +=1
        
        for letter in t:
            count[ord(letter)-ord("a")]-=1
        
        for c in count:
            if c!=0:
                return False

        return True