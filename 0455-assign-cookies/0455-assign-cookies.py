class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count, i, j = 0, 0, 0
        g.sort() # ===> O(mlogm)
        s.sort() # ===> O(nlogn)

        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                i+=1
                count+=1
            j+=1
        # ===> O(m)
        return count