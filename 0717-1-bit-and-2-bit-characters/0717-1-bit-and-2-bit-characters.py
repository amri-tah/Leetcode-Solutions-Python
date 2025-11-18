class Solution(object):
    def isOneBitCharacter(self, bits):
        i, n = 0, len(bits)
        while i<n-1:
            i += bits[i]+1
        return i == n-1