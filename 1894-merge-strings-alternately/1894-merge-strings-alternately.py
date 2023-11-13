class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        out = ""
        for i in range(max(len(word1), len(word2))):
            if i<len(word1) and i<len(word2):
                out+=word1[i]+word2[i]
            elif i<len(word1):
                out+=word1[i]
            else:
                out+=word2[i]
        return out
        